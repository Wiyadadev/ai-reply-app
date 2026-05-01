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
