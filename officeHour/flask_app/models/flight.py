from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import passenger


class Flight:
    db = 'week5session1'
    def __init__(self, data):
        self.id = data['id']
        self.origination = data['origination']
        self.destination = data['destination']
        self.departTime = data['departTime']
        self.arriveTime = data['arriveTime']
        self.flightNumber = data['flightNumber']
        self.passengers = []

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM flight;'
        results = connectToMySQL(cls.db).query_db(query)
        allFlights = []
        for row in results:
            flight = cls(row)
            allFlights.append(flight)
        return allFlights

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM flight WHERE id = %(id)s;'
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO flight (origination, destination, departTime, arriveTime, flightNumber) VALUES (%(origination)s, %(destination)s, %(departTime)s, %(arriveTime)s, %(flightNumber)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE flight SET origination=%(origination)s, destination=%(destination)s, departTime=%(departTime)s, arriveTime=%(arriveTime)s, flightNumber=%(flightNumber)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM flight WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def flightManifest(cls, data):
        query = 'SELECT * FROM flight LEFT JOIN passenger on passenger.flight_id = flight.id WHERE flight.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        # print("print results: ", results)
        flight = cls(results[0])
        for row in results:
            data = {
            'id': row['passenger.id'],
            'firstName': row['firstName'],
            'lastName': row['lastName'],
            'flight_id': row['flight_id']
            }
            p = passenger.Passenger(data)
            # print("The passenger data: ", p)
            flight.passengers.append(p)
            # print("passengers list: ", flight)
        return flight