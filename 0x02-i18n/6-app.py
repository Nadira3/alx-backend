#!/usr/bin/env python3
""" Handle locale parameter """
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)

# Mock user data for login
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Config class with languages and default locale
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

# Get user from mock database based on login_as URL parameter
def get_user():
    """ get user to log in """
    user_id = request.args.get("login_as")
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None

@app.before_request
def before_request():
    """ Set up g.user to be available globally """
    user = get_user()
    g.user = user

# Modified get_locale function with user locale priority
@babel.localeselector
def get_locale():
    """ Determines the best match for supported languages based on the request. """
    # First, check for the 'locale' URL parameter
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    
    # Second, check for the user’s preferred locale from g.user
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    
    # Third, use the request's Accept-Language header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """ Basic route to display welcome message """
    return render_template("6-index.html")

if __name__ == "__main__":
    app.run(debug=True)
