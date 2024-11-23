#!/usr/bin/env python3
""" Parameterize templates with Babel """
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ Configuration for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determines the best locale for the user.

    It checks the URL parameters, user settings, or request headers to
    select the most appropriate locale. Defaults to 'en' if no match is found.
    """
    # Logic for getting locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """
    Render the index page with a title and header.

    The title and header will be translated based on the selected locale.
    """
    return render_template("3-index.html",
                           title=_("home_title"), header=_("home_header"))


if __name__ == "__main__":
    """ Main function set to run """
    app.run(debug=True)
