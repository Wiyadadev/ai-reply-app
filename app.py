from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("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"))

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        return jsonify({"reply": response.choices[0].message.content})

    except Exception as e:
        return jsonify({"error": str(e)})




