#!/usr/bin/python3
"""A script that starts a flask web application"""
from flask import Flask, render_template

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

    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display python followed by a value"""

    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """display if in is int"""

    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number(n):
    """ display a HTML page only if n is an integer"""

    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def isOdd_isEven(n):
    """display a HTML page only if n is an integer"""

    even_or_odd = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html',
                           n=n, even_or_odd=even_or_odd)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
