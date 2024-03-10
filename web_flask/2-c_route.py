#!/usr/bin/python3
"""
This is a script that starts a Flask web application with three routes.
"""
from flask import Flask


# Name tells to look for resources.
app = Flask(__name__)


# Decorator to tell Flask what URL should trigger our function.
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


# Decorator to tell Flask what URL should trigger our function.
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


# Prevents the Flask dev server from starting if imported elsewhere.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
