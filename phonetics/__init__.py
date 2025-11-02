from flask import Flask
from flask_sqlalchemy import SQLAlchemy




# app = Flask(__name__)
# app.register_blueprint(home_routes)
# app.register_blueprint(user_routes)

# # app.config.from_object(Config)
# # Configure SQLite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning
# db.init_app(app)

# # Create SQLAlchemy instance
# db = SQLAlchemy(app)

def create_app():
    from phonetics.routes import home_routes, word_routes
    from phonetics.models import db
    from phonetics.config import Config
    from phonetics.seeding import seed_database

    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(word_routes)

    # app.config.from_object(Config)
    # Configure SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning
    db.init_app(app)
    with app.app_context():
        db.create_all()
        seed_database(db)

    return app

if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app = create_app()
    app.run(host="0.0.0.0", port=8080, debug=True)