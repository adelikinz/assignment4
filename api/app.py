from flask import Flask, request, jsonify
from db_utils import db_call_without_values, create_customer_db, db_call_with_values_without_return, db_call_with_values, find_customer_db, add_booking_to_db, cancel_bookings, update_pet_availability
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


@app.route('/rent', methods=['POST'])
def rent_pet():
    # endpoint to fill in the booking table for renting pet
    renting_data = request.json
    pet_id = renting_data.get('pet_id')
    customer_id = renting_data.get('customer_id')
    timeslot = renting_data.get('timeslot')
    booking_date = renting_data.get('booking_date')

    new_booking = add_booking_to_db(pet_id, customer_id, timeslot, booking_date)

    return jsonify(new_booking), 201


@app.route('/adopt', methods=['POST'])
def adopt_pet(data=None):
    adoption_data = request.json
    pet_id = data.get('pet_id')

    # Cancel any existing bookings for the pet due to pending adoption
    cancel_bookings(pet_id)

    # Update pet availability to not available for rent due to adoption
    update_pet_availability(pet_id)

    return jsonify({"message": "Successful adoption"}), 200



if __name__ == '__main__':
    app.run(debug=True, port=5000)
