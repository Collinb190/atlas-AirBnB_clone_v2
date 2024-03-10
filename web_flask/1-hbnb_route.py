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


# Prevents the Flask dev server from starting if imported elsewhere.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
