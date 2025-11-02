from flask import Blueprint, render_template
from phonetics.models import db, Phoneme, Word

home_routes = Blueprint('home', __name__)
word_routes = Blueprint('word', __name__)

@home_routes.route('/')
def home():
    # return "hello world"
    return render_template("pages/home.html")


@home_routes.route('/about')
def about():
    # return "about page"
    return render_template("pages/about.html")

@word_routes.route('/words')
def list_words():
    words = Word.query.all()
    return render_template("pages/words.html", words=words)