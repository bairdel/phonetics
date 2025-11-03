from phonetics.models import db, Phoneme, Word
from flask_sqlalchemy import SQLAlchemy
import os

def from_file():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Construct the path to the file in the parent directory
    with open(dir_path + '/data/phonemes.csv', 'r') as f:
        header = f.readline()  # Skip header line
        phonemes = [line.strip() for line in f.readlines()]
    with open(dir_path + '/data/words.csv', 'r') as f:
        header = f.readline()  # Skip header line
        words = [line.strip() for line in f.readlines()]

    return phonemes, words

def seed_database(db):
    # Clear existing data
    db.drop_all()
    db.create_all()

    phonemes, words = from_file()

    for p in phonemes:
        symbol, text, age = p.split(',')
        phoneme = Phoneme(symbol=symbol, text=text, age=age)
        db.session.add(phoneme)
    db.session.commit()

    
    for w in words:
        phonemes_ids = [None, None, None]
        text, initial, medial, final, phonemes_ids[0], phonemes_ids[1], phonemes_ids[2]  = w.split(',')
        phonemes_ids[0] = db.session.execute(db.select(Phoneme.id).where(Phoneme.symbol == phonemes_ids[0])).all()
        phonemes_ids[1] = db.session.execute(db.select(Phoneme.id).where(Phoneme.symbol == phonemes_ids[1])).all()
        phonemes_ids[2] = db.session.execute(db.select(Phoneme.id).where(Phoneme.symbol == phonemes_ids[2])).all()

        for p in range(len(phonemes_ids)):
            if len(phonemes_ids[p]) > 0:
                phonemes_ids[p] = phonemes_ids[p][0][0]
            else:
                phonemes_ids[p] = None

        word = Word(text=text, initial=initial, medial=medial, final=final, initial_phoneme=phonemes_ids[0], medial_phoneme=phonemes_ids[1], final_phoneme=phonemes_ids[2])
        db.session.add(word)

    # # Sample phonemes
    # phonemes = [
    #     Phoneme(symbol='p', equivalent='p as in "pat"'),
    #     Phoneme(symbol='b', equivalent='b as in "bat"'),
    #     Phoneme(symbol='t', equivalent='t as in "tap"'),
    #     Phoneme(symbol='d', equivalent='d as in "dog"'),
    # ]

    # # Sample words
    # words = [
    #     Word(text='pat', initial='p', medial='æ', final='t'),
    #     Word(text='bat', initial='b', medial='æ', final='t'),
    #     Word(text='tap', initial='t', medial='æ', final='p'),
    #     Word(text='dog', initial='d', medial='ɔ', final='g'),
    # ]

    # # Add to session and commit
    # db.session.add_all(phonemes + words)
    db.session.commit()

if __name__ == "__main__":
    from_file()