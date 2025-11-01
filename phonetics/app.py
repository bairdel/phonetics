from flask import Flask

from phonetics import pages

# @bp.route("/")
# def home():
#     return render_template("pages/home.html")

# @bp.route("/about")
# def about():
#     return render_template("pages/about.html")

class WSGILoggingMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print(f"Incoming request: {environ['REQUEST_METHOD']} {environ['PATH_INFO']}")
        return self.app(environ, start_response)

def create_app():
    app = Flask(__name__)
    # app.wsgi_app = WSGILoggingMiddleware(app.wsgi_app)  # Applying WSGI middleware
    app.register_blueprint(pages.bp)
    return app



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)