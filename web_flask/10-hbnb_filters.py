#!/usr/bin/python3
"""Starts a Flask web application to display the filter page"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display a HTML page with States, Cities, and Amenities"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=sorted_states, amenities=sorted_amenities)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

