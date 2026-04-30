from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/', methods=[GET', 'POST'])
def home():
    response = None

    if request. method == 'POST':
        user_input = request.form.get('user_input')
        response = "You said: "+ user_input

    return runder_template('index.html', response=response)

if __name__== '__main__':
    app.run()
  
