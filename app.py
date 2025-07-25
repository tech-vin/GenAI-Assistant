from flask import Flask, request, jsonify
from langchain_handler import process_prompt
from utils import save_memory, fetch_memory

app = Flask(__name__)

@app.route("/")
def index():
    return "👋 GenAI Resume Assistant is running!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "Missing 'question' field"}), 400

    response = process_prompt(question)
    return jsonify({"response": response})

@app.route("/memory", methods=["GET"])
def memory():
    return jsonify(fetch_memory())

if __name__ == "__main__":
    app.run(debug=True)
