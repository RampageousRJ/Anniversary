from flask import Flask, render_template,request,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
import sqlite3
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('ANNIVERSARY_SECRET_KEY')

db = sqlite3.connect('wishes.db', check_same_thread=False)

def create_table():
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS wishes (name TEXT, wish TEXT)')
    db.commit()

class WishesForm(FlaskForm):
    name = StringField('Enter name', validators=[DataRequired()])
    wish = TextAreaField('Enter the anniversary wish', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def home():
    create_table()
    form = WishesForm()
    if request.method=='POST':
        name = form.name.data
        wish = form.wish.data
        cursor = db.cursor()
        cursor.execute('INSERT INTO wishes (name, wish) VALUES (?,?)',(name,wish))
        db.commit()
    return render_template('home.html',form=form)

@app.route('/wishes')
def wishes():
    wishes = []
    cursor = db.cursor()
    cursor.execute('SELECT * FROM wishes')
    rows = cursor.fetchall()
    for row in rows:
        wishes.append(row)
    print(wishes)
    return render_template('wishes.html',wishes=wishes)

@app.route('/add-wish', methods=['GET','POST'])
def add_wishes():
    create_table()
    form = WishesForm()
    if request.method=='POST':
        name = form.name.data
        wish = form.wish.data
        cursor = db.cursor()
        cursor.execute('INSERT INTO wishes (name, wish) VALUES (?,?)',(name,wish))
        db.commit()
        flash('Anniversary wishes recorded! Thanks for your response!')
        form.wish.data,form.name.data = "",""
    return render_template('add-wish.html',form=form)