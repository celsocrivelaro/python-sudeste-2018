from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('welcome.html')

@app.route('/enviar')
def envia():
    return render_template('cadastrado.html')
