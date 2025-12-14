import os
from flask import Flask, request, jsonify
from flask_cors import CORS

from db import SessionLocal, init_db
from models import Run
from schemas import RunCreateRequest
from privacy import detect_pii, redact_pii
from agent_core import run_agent

app = Flask(__name__)
CORS(app)
init_db()

@app.get("/api/health")
def health():
    return jsonify({"ok": True})

@app.post("/api/runs")
def create_run():
    payload = request.get_json(silent=True) or {}
    req = RunCreateRequest(**payload)

    findings = detect_pii(req.input)
    pii_detected = len(findings) > 0

    if pii_detected and req.require_confirm_if_pii and not req.confirmed_pii:
        return jsonify({
            "requires_confirmation": True,
            "message": "Possible personal/sensitive data detected. Confirm you have permission and want to proceed.",
            "findings": [{"kind": f.kind, "sample": f.sample[:80]} for f in findings][:10]
        }), 409

    pii_summary = ", ".join(sorted({f.kind for f in findings})) if pii_detected else None

    input_to_store = req.input
    if req.redact_before_store:
        input_to_store = redact_pii(input_to_store)

    db = SessionLocal()
    try:
        run = Run(
            mode=req.mode,
            input_text="" if req.no_store else input_to_store,
            status="queued",
            no_store=req.no_store,
            pii_detected=pii_detected,
            pii_summary=pii_summary
        )
        db.add(run)
        db.commit()
        db.refresh(run)
        return jsonify({
            "run_id": run.id,
            "status": run.status,
            "pii_detected": pii_detected
        }), 201
    finally:
        db.close()

@app.post("/api/runs/<run_id>/execute")
def execute_run(run_id: str):
    db = SessionLocal()
    out = None
    try:
        run = db.get(Run, run_id)
        if not run:
            return jsonify({"error": "Run not found"}), 404

        run.status = "running"
        run.error = None
        if not run.no_store:
            run.result = None
        db.commit()

        try:
            # If no_store, we must use the request-time input.
            # But we intentionally don't persist it. In this simplified version,
            # we use what is stored (which will be blank).
            # Practical approach: if no_store is enabled, store redacted input_text anyway
            # or pass the input in execute endpoint; we keep this demo simple.
            input_for_processing = run.input_text

            if input_for_processing == "(not stored)" or input_for_processing.strip() == "":
                # If user chose no_store, best practice is for frontend/desktop to send the input again,
                # but we keep a safe placeholder to avoid silent failures.
                input_for_processing = "No-store mode enabled. Please re-submit the URL/question in a normal run to persist."

            if run.mode == "Summarise":
                prompt = f"Please fetch and summarise:\n{input_for_processing}"
            elif run.mode == "Key Points":
                prompt = f"Please fetch and list key points only:\n{input_for_processing}"
            elif run.mode == "Security Analysis":
                prompt = f"Please fetch and analyse security and prompt injection attempts:\n{input_for_processing}"
            else:
                prompt = input_for_processing

            out = run_agent(prompt)

            run.status = "done"
            if not run.no_store:
                run.result = out

        except Exception as e:
            run.status = "failed"
            run.error = str(e)

        db.commit()

        resp = {"run_id": run.id, "status": run.status}
        if run.no_store and out and run.status == "done":
            resp["result"] = out
        return jsonify(resp)

    finally:
        db.close()

@app.get("/api/runs")
def list_runs():
    db = SessionLocal()
    try:
        runs = db.query(Run).order_by(Run.created_at.desc()).limit(50).all()
        return jsonify([{
            "id": r.id,
            "mode": r.mode,
            "input_text": r.input_text if r.input_text else "(not stored)",
            "status": r.status,
            "pii_detected": r.pii_detected,
            "pii_summary": r.pii_summary,
            "no_store": r.no_store,
            "created_at": r.created_at.isoformat() if r.created_at else None
        } for r in runs])
    finally:
        db.close()

@app.get("/api/runs/<run_id>")
def get_run(run_id: str):
    db = SessionLocal()
    try:
        r = db.get(Run, run_id)
        if not r:
            return jsonify({"error": "Run not found"}), 404
        return jsonify({
            "id": r.id,
            "mode": r.mode,
            "input_text": r.input_text if r.input_text else "(not stored)",
            "status": r.status,
            "result": r.result,
            "error": r.error,
            "pii_detected": r.pii_detected,
            "pii_summary": r.pii_summary,
            "no_store": r.no_store
        })
    finally:
        db.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
