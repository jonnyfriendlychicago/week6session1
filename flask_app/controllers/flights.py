from flask_app import app
from flask import Flask, render_template,  redirect, session, request
from flask_app.models.flight import Flight
from flask_app.models.airline import Airline

@app.route('/flights/')
def flights():
    return render_template('flights.html', flights=Flight.getAll(), airlines=Airline.getAll())

@app.route('/flights/add/')
def addFlight():
    return render_template('addFlight.html', airlines=Airline.getAll())

@app.route('/flights/create/', methods=['POST'])
def createFlight():
    data = {
        'number': request.form['number'],
        'departing': request.form['departing'],
        'arriving': request.form['arriving'],
        'airline_id': request.form['airline_id'],
    }
    Flight.save(data)
    return redirect('/flights/')

@app.route('/flights/<int:flight_id>/view/')
def viewFlight(flight_id):
    data = {
        'id': flight_id
    }
    return render_template('viewFlight.html', flights=Flight.getOne(data), airlines=Airline.getAll())

@app.route('/flights/<int:flight_id>/edit/')
def editFlight(flight_id):
    data = {
        'id': flight_id
    }
    return render_template('editFlight.html', flights=Flight.getOne(data), airlines=Airline.getAll())

@app.route('/flights/<int:flight_id>/update/')
def updateFlight(flight_id):
    data = {
        'id': flight_id,
        'number': request.form['number'],
        'departing': request.form['departing'],
        'arriving': request.form['arriving'],
    }
    return redirect(f'/flights/{flight_id}/view/')

@app.route('/flights/<int:flight_id>/view/')
def deleteFlight(flight_id):
    data = {
        'id': flight_id,
    }
    Flight.delete(data)
    return redirect('/flights/')