from flask import Flask
from pymongo import MongoClient
from flask_googlemaps import GoogleMaps
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12).hex()

GoogleMaps(app, key="AIzaSyDVkiOWeis2ECi6UxP8CCdAYGZl3HmeTho")
client = MongoClient('localhost', 27017)
db = client.flask_db
# todos = db.todos

from webpage import routes