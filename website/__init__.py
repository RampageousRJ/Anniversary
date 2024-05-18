from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/wishes')
def wishes():
    return render_template('wishes.html')