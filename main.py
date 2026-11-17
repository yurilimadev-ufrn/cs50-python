from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "codigo flask ativo!"


app.run(debug=True)
