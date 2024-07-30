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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

