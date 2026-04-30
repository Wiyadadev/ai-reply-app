from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello from Python"
    response = None

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        response = "You said: " + user_input

    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run()
