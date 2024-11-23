#!/usr/bin/env python3
""" Use time zone module implementation """
from flask import Flask, request, g, render_template
from flask_babel import Babel
import pytz
from pytz import UnknownTimeZoneError

app = Flask(__name__)

# Mock user data for login
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Config class with languages and time zones
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

# Get user from mock database based on login_as URL parameter
def get_user():
    user_id = request.args.get("login_as")
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None

@app.before_request
def before_request():
    """ Set up g.user to be available globally """
    user = get_user()
    g.user = user

# Get Timezone function using babel.timezoneselector
@babel.timezoneselector
def get_timezone():
    """ Determines the best match for timezones based on the request. """
    # First, check for the 'timezone' URL parameter
    timezone = request.args.get('timezone')
    if timezone:
        try:
            # Validate the time zone
            pytz.timezone(timezone)  # This will raise UnknownTimeZoneError if invalid
            return timezone
        except UnknownTimeZoneError:
            return Config.BABEL_DEFAULT_TIMEZONE  # Fallback to UTC if invalid
    
    # Second, check for the user’s preferred timezone from g.user
    if g.user and g.user['timezone']:
        try:
            # Validate the user’s time zone
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            return Config.BABEL_DEFAULT_TIMEZONE  # Fallback to UTC if invalid
    
    # Default to the configured default timezone (UTC)
    return Config.BABEL_DEFAULT_TIMEZONE

@app.route('/')
def index():
    """ Basic route to display the current timezone """
    return render_template("7-index.html")

if __name__ == "__main__":
    app.run(debug=True)
