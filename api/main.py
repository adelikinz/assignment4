import json
import requests

host_url = 'http://127.0.0.1:5000'
# update to host url on device should be same url as the one given in flask

def display_availability():
    # sending a GET request to retrieve available pets
    response = requests.get(f'{host_url}/pets', headers={'content-type': 'application/json'})
    # Check if the response status code is OK (200)
    if response.status_code == 200:
    # if response = 200, extract data in JSON format
        pets = response.json()
        print("Available Pets:")
    # iterate over each pet and display their pet ID, Name, Type and Age:
        for pets in pets:
            print(f"ID: {pets[0]}, Name: {pets[1]}, Type: {pets[2]}, Age: {pets[3]}")
    else:
    # if response status code != 200, then print the below:
        print("Failed to retrieve available pets.")
# function for displaying the available pets:

def rent_pet(pet_id, timeslot, customer_id, date):
    url = f'{host_url}/rent'
    data = {'pet_id': pet_id, 'timeslot': timeslot, 'customer_id': customer_id, 'bookingDate': date}
# takes the user input for booking table and posts it to the endpoint (uses app endpoint /rent)

def adopt_pet(pet_id):
    url = f'{host_url}/adopt'
# removes any bookings and alters availability so noone is able to book the pet (uses app endpoint /adopt)

def create_customer(customer_name, customer_email):
    url = f'{host_url}/create_customer'
    data = {'customer_name': customer_name, 'customer_email': customer_email}
    response = requests.post(url, headers={'content-type': 'application/json'}, json=data)
    if response.status_code == 201:
        print("customer created successfully")
        response_data = response.json()
        customer_id = response_data.get('customer_id')
        return customer_id
    else:
        print("Failed to create customer")
        return None
# creates a customer with user input of name and email and saves them in the database as a customer (uses app endpoint /create_user)

def query_existing_customer(customer_name, customer_email):
    url = f'{host_url}/find_customer'
    data = {'customer_name': customer_name, 'customer_email': customer_email}
    response = requests.post(url, headers={'content-type': 'application/json'}, json=data)
    if response.status_code == 200:
        print("customer found successfully")
        customer_id = response.text
        return customer_id
    else:
        print("Failed to find customer")
        return None
# searches for existing customer using input of customer name and email in the database and returns the customer_id.

def display_dates(pet_id):
    url = f'{host_url}/dates'
    data = {'pet_id': pet_id}
# retrieves the available dates for the pet using the id,
# may also want a separate function to format the date itself using datetime


def display_timeslots(pet_id, bookingDate):
    url = f'{host_url}/timeslots'
    data = {'pet_id': pet_id, 'bookingDate': bookingDate}
# uses the inputted pet id and booking date to retrieve the available timeslots on that day (9-11am, 1-3pm or 5-7pm)
# may want another function to format user input as the headers in the database look like timeslot_9_11 etc)


def run():
    print('############################')
    print('Welcome to Pet Haven!')
    print('############################')
    print()

    while True:
        adopt_pet_choice = input('Would you like to rent or adopt one of our pets? (Type "exit" to quit) ').lower() # to format user input
        if adopt_pet_choice in ['rent', 'adopt', 'exit']:
            break
        else:
            print('Invalid choice. Please enter either "rent", "adopt" or "exit".')

    if adopt_pet_choice == 'rent':
        ## pet availability shown here ###
        pet_id = input('Enter the ID of the pet you would like to rent: ')
        ### dates available for selected pet id shown here ###
        date = input('Enter the date you would like to book (yyyy-mm-dd): ')
        ### available timeslots shown here ###
        # timeslot = user input here for selected timeslot

        customer = input('Are you a new customer? Enter yes or no: ')
        if customer == 'yes':
            customer_name = input("Enter customer name: ")
            customer_email = input("Enter customer email: ")
            customer_id = create_customer(customer_name, customer_email)
            if customer_id:
                rent_pet(pet_id, timeslot, customer_id, date)
            else:
                print("Failed to obtain customerid from new customer")
        else:
            customer_name = input("Enter customer name: ")
            customer_email = input("Enter customer email: ")
            customer_id = query_existing_customer(customer_name, customer_email)
            if customer_id:
                rent_pet(pet_id, timeslot, customer_id, date)
            else:
                print("Failed to obtain customer id from existing customer")
        # this is a loop for customer input

    elif adopt_pet_choice == 'adopt':
    ### show available pets here ###
        pet_id = input('Enter the ID of the pet you would like to adopt: ')
    ### activate adopt function here using pet id ###

    elif adopt_pet_choice == 'exit':
        print("Goodbye! We hope to see you again soon.")


if __name__ == '__main__':
    run()