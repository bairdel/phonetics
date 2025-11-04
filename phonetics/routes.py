from flask import Blueprint, render_template
from phonetics.models import db, Phoneme, Word

home_routes = Blueprint('home', __name__)
word_routes = Blueprint('word', __name__)

@home_routes.route('/')
def home():
    # return "hello world"
    phonetics = Phoneme.query.all()
    phonetics = sorted(phonetics, key=lambda p: p.text, reverse=False)
    phonetics = sorted(phonetics, key=lambda p: p.age, reverse=False)
    for p in phonetics:
        print(p.text)

    return render_template("pages/home.html", phonetics=phonetics)


@home_routes.route('/about')
def about():
    # return "about page"
    return render_template("pages/about.html")

@word_routes.route('/words')
def list_words():
    words = Word.query.all()
    return render_template("pages/words.html", words=words)

@word_routes.route('/phonetics/<phoneme_text>')
def phoneme_test(phoneme_text):
    phoneme = Phoneme.query.filter_by(text=phoneme_text).first()
    words = Word.query.filter_by(initial_phoneme=phoneme.id).all()
    words += Word.query.filter_by(medial_phoneme=phoneme.id).all()
    words += Word.query.filter_by(final_phoneme=phoneme.id).all()

    for w in words:
        print(w.text)

    if phoneme:
        return render_template("pages/phoneme.html", phoneme=phoneme, words=words)
        # return f"Phoneme: {phoneme.symbol}, Text: {phoneme.text}, Age: {phoneme.age}"
    else:
        return "Phoneme not found"
    
@word_routes.route('/phonetics/')
def phoneme_list():
    phonetics = Phoneme.query.all()
    phonetics = sorted(phonetics, key=lambda p: p.text, reverse=False)
    phonetics = sorted(phonetics, key=lambda p: p.age, reverse=False)
    return render_template("pages/phonetics.html", phonetics=phonetics)

