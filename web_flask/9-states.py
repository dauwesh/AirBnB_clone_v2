#!/usr/bin/python3
"""Starts a Flask web application to display a list of states and cities"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page with a list of states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)

@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """Display a HTML page with a list of cities of a state"""
    state = storage.all(State).get("State." + id)
    if state:
        sorted_cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states_by_id.html', state=state, cities=sorted_cities)
    else:
        return render_template('9-states_by_id.html', state=None)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

