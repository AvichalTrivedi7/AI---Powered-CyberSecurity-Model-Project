from flask import Flask, request, jsonify
from flask_cors import CORS
from llama_cpp import Llama

# === Load Mistral Model ===
llm = Llama(
    model_path="models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=2048,
    max_tokens=512,
    temperature=0.3,
    top_p=0.9,
    repeat_penalty=1.1
)

# === Flask App ===
app = Flask(__name__)
CORS(app)  # <-- Enable CORS so frontend (port 8000) can call backend (port 5000)

VALID_COMMANDS = ["open_door", "close_door", "emergency_stop"]

def classify_command(user_command: str) -> str:
    """
    Uses the LLM to classify metro commands into:
    - Valid - Normal
    - Invalid - Suspicious
    - Invalid - Malicious
    """
    prompt = f"""
You are a Metro Door Security AI. 
You must classify the following user command into one of three categories:
1. Valid - Normal
2. Invalid - Suspicious
3. Invalid - Malicious

Valid commands are strictly from this list: {VALID_COMMANDS}.
Check command length and wording to decide.

Command: {user_command}

Answer in only one line: 
Category = <Valid/Invalid>, Type = <Normal/Suspicious/Malicious>
"""
    response = llm(prompt, max_tokens=128, stop=["</s>"])
    return response["choices"][0]["text"].strip()


@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    user_command = data.get("command", "")
    if not user_command:
        return jsonify({"error": "No command provided"}), 400
    
    result = classify_command(user_command)
    return jsonify({"command": user_command, "classification": result})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"ok": True})


if __name__ == "__main__":
    # Visit http://127.0.0.1:5000/health to test
    app.run(host="0.0.0.0", port=5000, debug=True)
