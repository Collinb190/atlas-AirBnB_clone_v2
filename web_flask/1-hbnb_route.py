#!/usr/bin/python3
"""
This is a script that starts a Flask web application with two routes.
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


# Prevents the Flask dev server from starting if imported elsewhere.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
