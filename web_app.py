# web_app.py
from flask import Flask, render_template, request
from agent_app import run_agent

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if user_input:
            try:
                result = run_agent(user_input)
            except Exception as e:
                result = f"Error: {e}"

    return render_template("index.html", result=result, user_input=user_input)


if __name__ == "__main__":
    # host='0.0.0.0' will allow LAN access if firewall/network allows
    app.run(host="0.0.0.0", port=5000, debug=True)
