from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

SECRET_KEY = ''
DATABASE_URL = ''
DEBUG = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

## for use with config.py file option ##
if os.path.exists('main/config.py'):
    from .config import SECRET_KEY, DATABASE_URL, DEBUG, SQLALCHEMY_TRACK_MODIFICATIONS
    SECRET_KEY = SECRET_KEY
    DATABASE_URL = DATABASE_URL
    DEBUG = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = SQLALCHEMY_TRACK_MODIFICATIONS

app = Flask(__name__)

## for use with environment variables option ##
# secret_key_setting
if os.environ.get("SECRET_KEY"): SECRET_KEY = os.environ.get("SECRET_KEY")
app.config['SECRET_KEY'] = SECRET_KEY

# database_setting
if os.environ.get("DATABASE_URL"): DATABASE_URL = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

# debug_setting
if os.environ.get("DEBUG"): DEBUG = os.environ.get("DEBUG")
app.config['DEBUG'] = DEBUG

# sqlalchemy_modifications_setting
if os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS"): SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)

from . import routes
