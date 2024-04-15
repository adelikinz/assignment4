from flask import Flask, request, jsonify
from db_utils import (db_call_without_values, create_customer_db, db_call_with_values_without_return,
                      db_call_with_values, find_customer_db)


app = Flask(__name__)


@app.route('/pets', methods=['GET'])
def get_available_pets():
    # SQL query to retrieve available pets from DB:
    query = "SELECT * FROM pets WHERE available_for_rent = 1"
    # fetch available pets from DB
    pets = db_call_without_values(query)
    # available pets are returned in a JSON response:
    return jsonify(pets)
# endpoint to retrieve pets that are available


@app.route('/dates', methods=['GET'])
def get_available_dates():
    pet_id = request.args.get('pet_id')

    # Check if pet_id has been given
    if pet_id is None:
        return jsonify({'message': 'Pet ID is required'}), 400

    # Pass the pet_id value within the query to get all dates
    query = "SELECT bookingDate FROM pet_bookings WHERE pet_id = %s"
    available_dates = db_call_with_values(query, (pet_id,))

    return jsonify(available_dates)
# endpoint to retrieve available dates for the available pet


@app.route('/timeslots', methods=['GET'])
def get_available_timeslots():
    pet_id = request.args.get('pet_id')
    booking_date = request.args.get('bookingDate')

    # Check if pet_id has been given
    if pet_id is None:
        return jsonify({'message': 'Pet ID is required'}), 400

    # Check if pet_id has been given
    if booking_date is None:
        return jsonify({'message': 'Booking date is required'}), 400

    query = """
    SELECT
        timeslot_9_11,
        timeslot_13_15,
        timeslot_17_19
    FROM
        pet_bookings
    WHERE
        pet_id = %s
        AND (timeslot_9_11 IS NULL OR booking_id_9_11 IS NOT NULL)
        AND (timeslot_13_15 IS NULL OR booking_id_13_15 IS NOT NULL)
        AND (timeslot_17_19 IS NULL OR booking_id_17_19 IS NOT NULL)
        AND bookingDate = %s
    """

    available_timeslots = db_call_with_values(query, (pet_id, booking_date))

    # Create a dictionary with column names and corresponding timeslots
    timeslot_dict = {
        '9-11am': available_timeslots[0][0],
        '1-3pm': available_timeslots[0][1],
        '5-7pm': available_timeslots[0][2]
    }
    # Filter out None values and corresponding table headers
    filtered_timeslots = [timeslot for timeslot in timeslot_dict.values() if timeslot is None]
    filtered_table_headers = [header for header, timeslot in timeslot_dict.items() if timeslot is None]
    response_data = {
        'timeslots': [filtered_timeslots],
        'table_header': filtered_table_headers
    }

    return jsonify(response_data)
# endpoint to retrieve available timeslots for available pet


@app.route('/create_customer', methods=['POST'])
def create_customer():
    data = request.json
    customer_name = data.get('customer_name')
    customer_email = data.get('customer_email')

    # Checks if the required fields are provided
    if not customer_name or not customer_email:
        return jsonify({'message': 'Customer name and email are required'}), 400

    # Insert the new customer into the database and retrieves customer id for newly created customer
    try:
        query = "INSERT INTO customers (customer_name, customer_email) VALUES ('{}', '{}')".format(customer_name,
                                                                                                   customer_email)
        customer_id = create_customer_db(query)  # Calls the create_customer function with the query and values
        return jsonify({'message': 'User created successfully', 'customer_id': customer_id}), 201
    except Exception as e:
        return jsonify({'message': 'Failed to create user', 'error': str(e)}), 500
    # this endpoint creates a customer in the customer table and retrieves customer id for booking
# endpoint to create a customer in the database


@app.route('/find_customer', methods=['POST'])
def find_customer():
    data = request.json
    customer_name = data.get('customer_name')
    customer_email = data.get('customer_email')

    # Checks if the inputted fields are provided match the customer's in the database
    if not customer_name or not customer_email:
        return jsonify({'message': 'Customer name and email are required'}), 400

    # retrieves the returning customer's id from the database to be used for booking
    try:
        query = "SELECT customer_id FROM customers WHERE customer_name = %s AND customer_email = %s"
        customer_id = find_customer_db(query, (customer_name, customer_email))
        return str(customer_id[0][0])
    except Exception as e:
        return jsonify({'message': 'Failed to find customer', 'error': str(e)}), 500
#  this endpoint is to find existing customers in the database from customer name and email
#  and retrieves their customer id for booking


@app.route('/rent', methods=['POST'])
def rent_pet():
    # endpoint to fill in the booking table for renting pet
    renting_data = request.json
    pet_id = renting_data.get('pet_id')
    customer_id = renting_data.get('customer_id')
    timeslot = renting_data.get('timeslot')
    booking_date = renting_data.get('bookingDate')
    if not pet_id or not timeslot or not customer_id or not booking_date:
        return jsonify({'message': 'Missing required fields'}), 400

    try:
        booking_id_column = f"booking_id_{timeslot[9:]}"
        # Book the pet for the specified timeslot
        booking_query = (f"UPDATE pet_bookings SET {timeslot} = %s, "
                         f"{booking_id_column} = %s WHERE pet_id = %s AND bookingDate = %s")
        db_call_with_values_without_return(booking_query, (customer_id, customer_id, pet_id, booking_date))
        return jsonify({'message': 'Pet rented successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Failed to rent pet', 'error': str(e)}), 500
# endpoint to fill in booking table


@app.route('/adopt', methods=['POST'])
def adopt_pet():
    data = request.json
    pet_id = data.get('pet_id')

    # updates the availability of the pet for adoption
    query = "UPDATE pets SET available_for_rent = 0 WHERE pet_id = %s"
    db_call_with_values_without_return(query, (pet_id,))

    # Remove the pet from the available pets list
    query = "DELETE FROM pet_bookings WHERE pet_id = %s"
    db_call_with_values_without_return(query, (pet_id,))

    return jsonify({'message': 'Pet adopted successfully and bookings deleted'}), 200
# endpoint to update availability


if __name__ == '__main__':
    app.run(debug=True, port=5000)
