from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.flight import Flight
from flask_app.models.passenger import Passenger

@app.route('/addPassenger/')
def addPassenger():
    print(Flight.getAll())
    return render_template('addPassenger.html',flights=Flight.getAll())

@app.route('/createPassenger/', methods=['POST'])
def createPassenger():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'flight_id': request.form['flight_id']
    }
    Passenger.save(data)
    return redirect('/')

@app.route('/passenger/<int:passenger_id>/view/')
def viewPassenger(passenger_id):
    data = {
        'id': passenger_id
    }
    return render_template('viewPassenger.html', user=Passenger.getOne(data), flights=Flight.getAll())

@app.route('/passenger/<int:passenger_id>/update/', methods=['POST'])
def updatePassenger(passenger_id):
    data = {
        'id': passenger_id,
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'flight_id': request.form['flight_id']
    }
    Passenger.update(data)
    return redirect(f'/passenger/{passenger_id}/view/')

@app.route('/passenger/<int:passenger_id>/delete/')
def deletePassenger(passenger_id):
    data = {
        'id': passenger_id
    }
    Passenger.delete(data)
    return redirect('/')