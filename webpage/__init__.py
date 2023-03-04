from flask import Flask
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12).hex()
from webpage import routes