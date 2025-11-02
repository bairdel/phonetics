
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Phoneme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    equivalent = db.Column(db.String(100), nullable=True)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), unique=True, nullable=False)
    initial = db.Column(db.String(200), nullable=True)
    medial = db.Column(db.String(200), nullable=True)
    final = db.Column(db.String(200), nullable=True)

