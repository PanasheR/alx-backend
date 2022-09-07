#!/usr/bin/env python3
""" Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    ''' babelconfig class '''
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'


@babel.localeselector
def get_locale():
    ''' get_locale from request '''
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"])
def index():
    """ returns index """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
