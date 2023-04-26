#!/usr/bin/env python3
""" Creating Flask application """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)  # Initialize Babel


class Config(object):   # Configure available languages
    """ Config class """
    LANGUAGES = ["en", "fr"]    # English and French
    BABEL_DEFAULT_LOCALE = "en"  # Default language
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app.config.from_object(Config)  # Load config class


@app.route('/', strict_slashes=False)
def index():
    """ Creating index page """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
