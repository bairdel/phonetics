from flask import Flask

from phonetics import pages


app = Flask(__name__)
app.register_blueprint(pages.bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)