from datetime import datetime
from website import database

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    profile_img = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='owner', lazy=True)
    knowledge = database.Columns(database.String, nullable=False, default='Unknown')
    
class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String, nullable=False)
    content = database.Column(database.Text, nullable=False)
    creation_data = database.Column(database.DateTime, nullable=False, defaut=datetime.utcnow)
    id_user = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
    
if __name__ == '__main__':
    from website import database
    from models import User, Post
    database.create_all()