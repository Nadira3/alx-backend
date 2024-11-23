#!/usr/bin/env python3
""" Force get_locale """
from flask import Flask, render_template, request
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


app = Flask(__name__)


# Set up Flask Babel
class Config:
    """ Configuration for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


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


# Home route
@app.route("/")
def index():
    """ Render the homepage """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
