from flask import Flask

from phonetics import pages


app = Flask(__name__)
app.register_blueprint(pages.bp)