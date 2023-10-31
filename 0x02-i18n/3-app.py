#!/usr/bin/env python
"""
Parametrize templates
"""
from flask import Flask, render_template, request
from flask_babel import Babel
from flask_babel import _, gettext


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


@babel.localeselector
def get_locale():
    """
    the localeselection function
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    the route
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
