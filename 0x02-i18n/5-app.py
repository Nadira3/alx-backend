#!/usr/bin/env python3
""" Mock login module """
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


# Set up Flask Babel
class Config:
    """ Configuration for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# Function to get user from URL parameters
def get_user():
    user_id = request.args.get('login_as', type=int)
    if user_id and user_id in users:
        return users[user_id]
    return None


# Function to get locale based on URL parameter or other methods
@babel.localeselector
def get_locale():
    """ Determine the best match with supported languages """
    # Check if locale is passed as URL parameter
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    # Fallback to accept languages
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# Before request to set global user
@app.before_request
def before_request():
    g.user = get_user()


# Index route
@app.route('/')
def index():
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
