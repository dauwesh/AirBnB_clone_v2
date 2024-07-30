#!/usr/bin/python3
"""
A simple Flask web application that displays different messages
for different routes.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' when accessing the root route.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' when accessing the /hbnb route.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays 'C ' followed by the value of the text variable,
    with underscores replaced by spaces.
    """
    return "C {}".format(text.replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays 'Python ' followed by the value of the text variable,
    with underscores replaced by spaces. The default value of text is 'is cool'.
    """
    return "Python {}".format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

