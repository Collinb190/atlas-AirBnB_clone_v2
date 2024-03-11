#!/usr/bin/python3
"""
This is a script that starts a Flask web application with three routes.
"""
from flask import Flask


# Name tells flask to look for resources in the folder with this module.
app = Flask(__name__)
# Treats URLs with and without a trailing slash as the same.
app.url_map.strict_slashes = False


# Decorator to tell Flask what URL should trigger our function.
@app.route('/')
def hello():
    """
    Displays a message.
    """
    return 'Hello HBNB!'


# Decorator to tell Flask what URL should trigger our function.
@app.route('/hbnb')
def hbnb():
    """
    Displays a message.
    """
    return 'HBNB'


# Decorator to tell Flask what URL should trigger our function.
@app.route('/c/<text>')
def c_text(text):
    """
    Display “C ” followed by the value of the text variable.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


# Decorator to tell Flask what URL should trigger our function.
@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """
    Display “Python ”, followed by the value of the text variable.
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


# Decorator to tell Flask what URL should trigger our function.
@app.route('/number/<int:n>')
def show_number(n):
    """
    Display “n is a number” only if n is an integer.
    """
    return '{} is a number'.format(n)


# Prevents the Flask dev server from starting if imported elsewhere.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
