from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import flight


class Passenger:
    db = 'week5session1'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.flight_id = data['flight_id']

    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM passenger;'
        results = connectToMySQL(cls.db).query_db(query)
        print("all results model line 16: ", results)
        allPassengers = []
        for row in results:
            passenger = cls(row)
            print("model line 19: ", passenger)
            allPassengers.append(cls(row))
        return allPassengers

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM passenger WHERE id = %(id)s;'
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO passenger (firstName, lastName, flight_id) VALUES (%(firstName)s, %(lastName)s, %(flight_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE passenger SET firstName=%(firstName)s, lastName=%(lastName)s, flight_id=%(flight_id)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM passenger WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)