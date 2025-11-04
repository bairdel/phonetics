
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Phoneme(db.Model):
    __tablename__ = "phoneme_table"
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    text = db.Column(db.String(100), nullable=True)
    child_age = db.Column(db.Integer, nullable=True)

class Word(db.Model):
    __tablename__ = "words_table"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), unique=True, nullable=False)
    initial = db.Column(db.String(200), nullable=True)
    medial = db.Column(db.String(200), nullable=True)
    final = db.Column(db.String(200), nullable=True)
    initial_phoneme = db.Column(db.Integer, db.ForeignKey('phoneme_table.id'), nullable=True)
    medial_phoneme = db.Column(db.Integer, db.ForeignKey('phoneme_table.id'), nullable=True)
    final_phoneme = db.Column(db.Integer, db.ForeignKey('phoneme_table.id'), nullable=True)
    image_credit = db.Column(db.String(500), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
