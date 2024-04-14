from flask import Flask, request, jsonify
from db_utils import db_call_without_values, create_customer_db, db_call_with_values_without_return, db_call_with_values, find_customer_db
app = Flask(__name__)

# endpoint to retrieve pets that are available using GET HTTP
@app.route('/pets', methods=['GET'])
def get_available_pets():
    # SQL query to retrieve available pets from DB:
    query = "SELECT * FROM pets WHERE available_for_rent = 1"
    # fetch available pets from DB
    pets = db_call_without_values(query)
    # available pets are returned in a JSON response:
    return jsonify(pets)



@app.route('/dates', methods=[])
def get_available_dates():
    pass
# endpoint to retrieve available dates


@app.route('/timeslots', methods=[])
def get_available_timeslots():
    pass
# endpoint to retrieve available timeslots for the available pets


@app.route('/create_customer', methods=[])
def create_customer():
    pass
# endpoint to create a customer in the customer table as a user


@app.route('/find_customer', methods=[])
def find_customer():
    pass
# endpoint to find an existing customer as a user


@app.route('/rent', methods=[])
def rent_pet():
    pass
# endpoint to fill in the booking table for renting


@app.route('/adopt', methods=[])
def adopt_pet():
    pass
# endpoint for adopting where it cancels any existing bookings and removes pet from availability


if __name__ == '__main__':
    app.run(debug=True, port=5000)
