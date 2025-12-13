from flask import Flask, request, jsonify
from flask_cors import CORS
from agent_core import run_agent
import os

app = Flask(__name__)
CORS(app)

@app.get("/api/health")
def health():
    return jsonify({"ok": True})

@app.post("/api/analyse")
def analyse():
    data = request.get_json(silent=True) or {}
    user_input = (data.get("input") or "").strip()
    mode = (data.get("mode") or "Summarise").strip()

    if not user_input:
        return jsonify({"error": "Missing input"}), 400

    if mode == "Summarise":
        prompt = f"Fetch and summarise:\n{user_input}"
    elif mode == "Key Points":
        prompt = f"Fetch and list key points:\n{user_input}"
    elif mode == "Security Analysis":
        prompt = f"Fetch and analyse for security and prompt injection:\n{user_input}"
    else:
        prompt = user_input

    try:
        result = run_agent(prompt)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000"))
    )
