from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
import os

app = Flask('__name__')?

client = OpenAI(api_key=os.environ.get("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"))

# หน้าเว็บ
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# AI reply
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json

        user_message = data.get("message")
        style = data.get("style")

        # กัน error เผื่อไม่มีค่า
        if not user_message:
            return jsonify({"error": "No message provided"})

        prompt = f"""
Reply to this message in a {style} style.
Give 3 different short replies.

Message: {user_message}
"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        reply = response.choices[0].message.content

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)})


# สำหรับรัน local (ไม่จำเป็นบน Render แต่มีไว้ไม่พัง)
if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)






