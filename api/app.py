from flask import Flask, request, jsonify
from db_utils import db_call_without_values, create_customer_db, db_call_with_values_without_return, db_call_with_values, find_customer_db, add_booking_to_db, cancel_bookings, update_pet_availability
app = Flask(__name__)

@app.route('/pets', methods=[])
def get_available_pets():
    # endpoint to retrieve pets that are available
    pass


@app.route('/dates', methods=[])
def get_available_dates():
    # endpoint to retrieve available dates
    pass


@app.route('/timeslots', methods=[])
def get_available_timeslots():
    # endpoint to retrieve available timeslots for the available pets
    pass

@app.route('/create_customer', methods=[])
def create_customer():
    # endpoint to create a customer in the customer table as a user
    pass


@app.route('/find_customer', methods=[])
def find_customer():
    # endpoint to find an existing customer as a user
    pass

@app.route('/rent', methods=['POST'])
def rent_pet():
    # endpoint to fill in the booking table for renting
    renting_data = request.json
    pet_id = renting_data.get('pet_id')
    customer_id = renting_data.get('customer_id')
    timeslot = renting_data.get('timeslot')
    booking_date = renting_data.get('booking_date')

    new_booking = add_booking_to_db(pet_id, customer_id, timeslot, booking_date)

    return jsonify(new_booking), 201


# endpoint for adopting where it cancels any existing bookings and removes pet from availability
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
