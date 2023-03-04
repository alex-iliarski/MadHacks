from webpage import app
from flask import render_template, redirect, url_for, flash
from webpage import db
from flask_login import login_user, logout_user, login_required

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


