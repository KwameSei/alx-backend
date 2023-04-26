#!/usr/bin/env python3
""" Creating Flask application """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext, get_locale

app = Flask(__name__)
babel = Babel(app)  # Initialize Babel


class Config(object):   # Configure available languages
    """ Config class """
    LANGUAGES = ["en", "fr"]    # English and French
    BABEL_DEFAULT_LOCALE = "en"  # Default language
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app.config.from_object(Config)  # Load config class


#  Invoking the Babel object’s localeselector decorator to translate languages
@babel.localeselector
def get_locale():
    """ Getting the locale language for each request"""
    app_config = app.config['LANGUAGES']    # Get languages from config file
    locale_request = request.accept_languages.best_match(app_config)

    # Check if locale is provided in request arguments
    if 'locale' in request.args and request.args['locale'] in app_config:
        return request.args['locale']
    # Otherwise, use default behavior to find the best language match
    return locale_request  # Return best language match


@app.route('/', strict_slashes=False)
def index():
    """ Creating index page """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
