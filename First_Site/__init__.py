from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)

app.config['SECRET_KEY'] = 'I15NxqBiJ7R9nnUWhM3Nd5dCu3TUM8su'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from First_Site import pages