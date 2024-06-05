#!/usr/bin/python3
"""A script that starts a flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display hello hbnb"""

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display hbnb"""

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display C followed by the value of text variable"""

    return "C %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
