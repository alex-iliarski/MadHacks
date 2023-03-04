from webpage import app
from flask import render_template, redirect, url_for, flash

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# @app.route('/register')
# def register():
#     return render_template('register.html')