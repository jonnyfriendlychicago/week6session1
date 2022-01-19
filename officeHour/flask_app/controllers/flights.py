from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.flight import Flight
from flask_app.models.passenger import Passenger


@app.route('/')
def index():
    print(Passenger.getAll())
    return render_template('index.html', flights=Flight.getAll(), users=Passenger.getAll())

@app.route('/addFlight/')
def addFlight():
    return render_template('addFlight.html')

@app.route('/createFlight/', methods=['POST'])
def createFlight():
    data = {
        'origination': request.form['origination'],
        'destination': request.form['destination'],
        'departTime': request.form['departTime'],
        'arriveTime': request.form['arriveTime'],
        'flightNumber': request.form['flightNumber']
    }
    Flight.save(data)
    return redirect('/')

@app.route('/flight/<int:flight_id>/view/')
def viewFlight(flight_id):
    data = {
        'id': flight_id
    }
    return render_template('viewFlight.html', flight=Flight.getOne(data))

@app.route('/flight/<int:flight_id>/update/', methods=['POST'])
def updateFlight(flight_id):
    data = {
        'id': flight_id,
        'origination': request.form['origination'],
        'destination': request.form['destination'],
        'departTime': request.form['departTime'],
        'arriveTime': request.form['arriveTime'],
        'flightNumber': request.form['flightNumber']
    }
    Flight.update(data)
    return redirect(f'/flight/{flight_id}/view/')

@app.route('/flight/<int:flight_id>/delete/')
def deleteFlight(flight_id):
    data = {
        'id': flight_id
    }
    Flight.delete(data)
    return redirect('/')

@app.route('/flight/<int:flight_id>/manifest/')
def flightManifest(flight_id):
    data = {
        'id': flight_id
    }
    manifest=Flight.flightManifest(data)
    # print("manifest: ", manifest)
    return render_template('viewManifest.html', manifest=manifest)