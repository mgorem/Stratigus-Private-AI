from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import run_agent

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

    # Convert UI mode into a consistent prompt
    if mode == "Summarise":
        prompt = f"Fetch the webpage and summarise it:\n{user_input}"
    elif mode == "Key Points":
        prompt = f"Fetch the webpage and list key points only:\n{user_input}"
    elif mode == "Security Analysis":
        prompt = f"Fetch the webpage and analyse for risks and prompt injection attempts:\n{user_input}"
    else:
        prompt = user_input

    try:
        result = run_agent(prompt)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
