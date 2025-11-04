from flask import Blueprint, render_template, request
from phonetics.models import db, Phoneme, Word

home_routes = Blueprint('home', __name__)
word_routes = Blueprint('word', __name__)

@home_routes.route('/')
def home():
    # return "hello world"
    phonetics = Phoneme.query.all()
    phonetics = sorted(phonetics, key=lambda p: p.text, reverse=False)
    phonetics = sorted(phonetics, key=lambda p: p.child_age, reverse=False)
    ages = []
    for p in phonetics:
        print(p.text)
    [ages.append(val.child_age) for val in phonetics if val.child_age not in ages]
    print(ages)

    return render_template("pages/home.html", phonemes=phonetics, ages=ages)


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

    if phoneme:
        return render_template("pages/phoneme.html", phoneme=phoneme, words=words)
        # return f"Phoneme: {phoneme.symbol}, Text: {phoneme.text}, Age: {phoneme.age}"
    else:
        return "Phoneme not found"
    
@word_routes.route('/phonetics/')
def phoneme_list():
    phonetics = Phoneme.query.all()
    phonetics = sorted(phonetics, key=lambda p: p.text, reverse=False)
    phonetics = sorted(phonetics, key=lambda p: p.child_age, reverse=False)
    return render_template("pages/phonetics.html", phonetics=phonetics)

@word_routes.route('/test', methods=['GET','POST'])
def testing():
    phoneme = []
    allwords = False
    
    all_phonemes = Phoneme.query.all()
    if request.form:
        data = request.form
        if 'age' in data:
            age = int(data['age'])
        else: 
            age = 0

        for i in range(len(all_phonemes)):
            if "phoneme-" + str(all_phonemes[i].id) in data:
                phoneme.append(all_phonemes[i])
        if 'allwords' in data:
            if data['allwords'] == 'on':
                allwords = True
            else:
                allwords = False
    else:
        # if not entered from a form
        age = 0
        phoneme = []
        allwords = False

    # if phonemes selected disregard age selection
    if len(phoneme) > 0:
        age = 0

    words = []

    if allwords:
        words += Word.query.all()
    elif len(phoneme) == 1:
        # phoneme = Phoneme.query.filter_by(text=phoneme).first()
        words += Word.query.filter_by(initial_phoneme=phoneme.id).all()
        words += Word.query.filter_by(medial_phoneme=phoneme.id).all()
        words += Word.query.filter_by(final_phoneme=phoneme.id).all()
    elif len(phoneme) > 1:
        for p in phoneme:
            # phoneme = Phoneme.query.filter_by(text=phoneme).first()
            words += Word.query.filter_by(initial_phoneme=p.id).all()
            words += Word.query.filter_by(medial_phoneme=p.id).all()
            words += Word.query.filter_by(final_phoneme=p.id).all()
    elif age > 0:
        phoneme = Phoneme.query.filter(Phoneme.child_age <= age).all()
        for p in phoneme:
            print(p.text)
            words += Word.query.filter_by(initial_phoneme=p.id).all()
            words += Word.query.filter_by(medial_phoneme=p.id).all()
            words += Word.query.filter_by(final_phoneme=p.id).all()
    else:
        words += Word.query.all()

    res = []
    [res.append(val) for val in words if val not in res]
    words = res

    return render_template("pages/testing.html", words=words, phonemes = phoneme, agerange=age)

@word_routes.route('/results', methods=['POST'])
def results():
        # Get the form data as Python ImmutableDict datatype 
    data = request.form
    print(data)
    ## Return the extracted information 
    return render_template("pages/results.html")