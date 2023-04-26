#!/usr/bin/env python3
""" Creating Flask application """
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext, get_locale


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user(user_id):
    """ Function to return user dictionary or None """
    user = users.get(int(user_id))
    # if user_id in users:
    #     return users.get(user_id)
    # return None
    if user:
        return user
    return None

@app.before_request
def before_request():
    """ Find a user if any, and set it as a global on flask.g.user """
    user_id = request.args.get('login_as')
    if user_id:
        user = get_user(int(user_id))
        if user:
            g.user = user
    else:
        g.user = None

@app.route('/', strict_slashes=False)
def index():
    """ Creating index page """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
