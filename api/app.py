from flask import Flask, request, jsonify
from db_utils import db_call_without_values, create_user_db, db_call_with_values_without_return, db_call_with_values, find_user_db
app = Flask(__name__)

@app.route('/pets', methods=[])
def get_available_pets():
# endpoint to retrieve pets that are available


@app.route('/dates', methods=[])
def get_available_dates():
# endpoint to retrieve available dates


@app.route('/timeslots', methods=[])
def get_available_timeslots():
# endpoint to retrieve available timeslots for the available pets


@app.route('/create_customer', methods=[])
def create_customer():
# endpoint to create a customer in the customer table as a user


@app.route('/find_customer', methods=[])
def find_customer():
# endpoint to find an existing customer as a user


@app.route('/rent', methods=[])
def rent_pet():
# endpoint to fill in the booking table for renting


@app.route('/adopt', methods=[])
def adopt_pet():
# endpoint for adopting where it cancels any existing bookings and removes pet from availability


if __name__ == '__main__':
    app.run(debug=True, port=5000)
