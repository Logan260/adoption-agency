from flask_sqlalchemy import SQLAlchemy
from flask import Flask


db = SQLAlchemy()
app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "peanutbutter"
db.init_app(app)



class Pet(db.Model):
    """Adopt table"""
    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text , nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    available = db.Column(db.Boolean, nullable = False, default = True)

