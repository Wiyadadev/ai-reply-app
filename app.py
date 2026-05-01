from flask import Flask, render_template, request
import os
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    
    if request.method == "POST":
        text = request.form.get("text") or ""

        try:
            response = client.chat.completions.create(
                model="gpt-40-mini",
                messages=[
                    {"role": "user", "content": text}
                ]
            )

            result= response.choices[0].message.content
        except Exception as e:
            result = str(e)

    return render_template("index.html", result=result)


if __name__== "_main_":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
