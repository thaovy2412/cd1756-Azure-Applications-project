"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
app.logger.addHandler(streamHandler)
Session(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
