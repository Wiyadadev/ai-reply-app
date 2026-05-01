from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        text = request.form.get("text")
        result = f"You said: {text}"

    return render_template("index.html", result=result)

if __name__== "_main_":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
