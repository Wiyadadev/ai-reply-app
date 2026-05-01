from flask import Flask, render_template, request
import os
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("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"))

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    
    if request.method == "POST":
        text = request.form.get("text")
        
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": text}]
        )

        result = response.choices[0].message.content

    return render_template("index.html", result=result)


if __name__== "_main_":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
