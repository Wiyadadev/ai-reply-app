from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""

    if request.method == "POST":
        user_message = request.form.get("message", "")
        reply = "คุณพิมพ์ว่า: " + user_message

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
