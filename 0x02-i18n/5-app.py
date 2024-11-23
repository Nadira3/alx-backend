#!/usr/bin/env python3
""" Mock login module """
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)
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


# Function to get the locale from URL parameter or user settings
@babel.localeselector
def get_locale():
    # Check if 'locale' is passed in the URL, otherwise
    # fallback to user's locale or the default locale
    locale = request.args.get('locale')
    if locale:
        return locale
    if g.user and g.user.get('locale'):
        return g.user['locale']
    return request.accept_languages.best_match(['en', 'fr'])


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
