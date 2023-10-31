#!/usr/bin/env python3
"""
Get locale from request
"""
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Union
from flask import g


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

# Initialize Babel with the app instance
babel = Babel(app)


@app.before_request
def before_request():
    """
    before_request Function
    """
    g.user = get_user()


def get_user():
    """
    User login
    """
    user_id = request.args.get('login_as')
    if user_id:
        user = users.get(int(user_id))
        if user:
            return user
    return None


@babel.localeselector
def get_locale():
    """Locale from URL parameters"""
    requested_locale = request.args.get('locale')
    if requested_locale in app.config['LANGUAGES']:
        return requested_locale

    # Locale from user settings
    if g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    # Locale from request header
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    if best_match:
        return best_match

    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """ Greeting

        Return:
            Initial template html
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
