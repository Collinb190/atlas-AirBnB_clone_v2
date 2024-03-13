#!/usr/bin/python3
"""
This is a script that starts a Flask web application with three routes.
"""
from flask import Flask, render_template
from models import storage
from models import *


# Name tells flask to look for resources in the folder with this module.
app = Flask(__name__)
# Treats URLs with and without a trailing slash as the same.
app.url_map.strict_slashes = False


# Decorator to tell Flask what URL should trigger our function.
@app.route('/states')
@app.route('/states/<state_id>')
def states(state_id=None):
    """
    Displays the cities and states in order A-Z.
    """
    states = storage.all('State')
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template("9-states.html", states=states, state_id=state_id)


# Decorator to tell Flask to handle the teardown.
@app.teardown_appcontext
def take_down(self):
    """
    Method to handle the teardown.
    """
    storage.close()


# Prevents the Flask dev server from starting if imported elsewhere.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
