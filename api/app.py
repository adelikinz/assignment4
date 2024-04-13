from flask import Flask, jsonify, request
from db_utils import db_pethaven_overview, db_pet_id, add_booking_to_db


app = Flask(__name__)


# API endpoint to see all pets
@app.route('/pets', methods=['GET'])
def get_all_pets():
    pets = db_pethaven_overview()
    return jsonify(pets)


# API endpoint to get a specific pet by its id
@app.route('/pets/<int:pet_id>')
def get_pet_by_id(pet_id):
    res = db_pet_id(pet_id)
    return jsonify(res)

# API endpoint to add a booking
@app.route('/pet-bookings', methods=['POST'])
def appt_booking():
    booking_data = request.json

    pet_id = booking_data.get('pet_id')
    customer_id = booking_data.get('customer_id')
    timeslot = booking_data.get('timeslot')
    booking_date = booking_data.get('booking_date')

    new_booking = add_booking_to_db(pet_id, customer_id, timeslot, booking_date)

    return jsonify(new_booking), 201

if __name__ == '__main__':
    app.run(debug=True, port=5004)
