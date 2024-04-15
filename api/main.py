import json
import requests
from datetime import datetime

host_url = 'http://127.0.0.1:5000'
# update to host url on device (this should be the same url as the one given from flask)


def display_availability():
    response = requests.get(f'{host_url}/pets', headers={'content-type': 'application/json'})
    if response.status_code == 200:
        pets = response.json()
        print("Available Pets:")
        for pets in pets:
            print(f"ID: {pets[0]}, Name: {pets[1]}, Type: {pets[2]}, Age: {pets[3]}")
    else:
        print("Failed to retrieve available pets.")
# function for displaying the available pets:


def rent_pet(pet_id, timeslot, customer_id, date):
    url = f'{host_url}/rent'
    data = {'pet_id': pet_id, 'timeslot': timeslot, 'customer_id': customer_id, 'bookingDate': date}
    response = requests.post(url, headers={'content-type': 'application/json'}, json=data)
    print(response.json())
# function to update the booking table for renting


def adopt_pet(pet_id):
    url = f'{host_url}/adopt'
    data = {'pet_id': pet_id}
    response = requests.post(url, headers={'content-type': 'application/json'}, json=data)
    print(response.json())
# function that removes any bookings and alters availability to remove the pet from the available pet list


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
# function that creates a customer with given name and email and saves them in the database as a customer.


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
# function that searches for existing customer using given customer name and email
# this also returns the customer_id.


def display_dates(pet_id):
    url = f'{host_url}/dates'
    data = {'pet_id': pet_id}
    response = requests.get(url, headers={'content-type': 'application/json'}, params=data)

    if response.status_code == 200:
        response_data = response.json()

        list_of_available_dates = []

        # Create a list of dates displayed as ['YYYY-MM-DD']
        for main_list in response_data:
            for date_list in main_list:
                date_obj = datetime.strptime(date_list, '%a, %d %b %Y %H:%M:%S %Z')
                formatted_date_str = date_obj.strftime('%Y-%m-%d')
                list_of_available_dates.append(formatted_date_str)

        print("Available dates: ", list_of_available_dates)
        return list_of_available_dates

    else:
        print("Failed to retrieve available dates.")
        return None
# retrieves the available dates for the pet using it's given id


def display_timeslots(pet_id, booking_date):
    url = f'{host_url}/timeslots'
    data = {'pet_id': pet_id, 'bookingDate': booking_date}
    response = requests.get(url, headers={'content-type': 'application/json'}, params=data)
    try:
        data = response.json()
        timeslots = data['timeslots']
        if timeslots:
            filtered_table_headers = data['table_header']
            print("Available time slots:", filtered_table_headers)
        else:
            print("No timeslots available.")
    except json.decoder.JSONDecodeError:
        print("Invalid JSON response:", response.text)
    timeslots = response.json()
# retrieves the available timeslots for a specific pet on a specific date


def get_timeslot_choice():
    while True:
        timeslot = input('Enter the timeslot you would like to book (9-11am, 1-3pm, 5-7pm): ')
        if timeslot == '9-11am':
            return 'timeslot_9_11'
        elif timeslot == '1-3pm':
            return 'timeslot_13_15'
        elif timeslot == '5-7pm':
            return 'timeslot_17_19'
        else:
            print('Invalid timeslot. Please enter a valid timeslot.')
# formats user input for timeslot choice


def run():
    print('############################')
    print('Welcome to Pet Haven!')
    print('############################')
    print()

    while True:
        adopt_pet_choice = input('Would the customer like to rent or adopt one of our pets? ("exit" to quit) ').lower()
        if adopt_pet_choice in ['rent', 'adopt', 'exit']:
            break
        else:
            print('Invalid choice. Please enter either "rent", "adopt" or "exit".')

    if adopt_pet_choice == 'rent':
        print()
        display_availability()

        while True:
            pet_id = input('\nEnter the ID of the pet you would like to rent: ')
            response = requests.get(f'{host_url}/pets', headers={'content-type': 'application/json'})
            if response.status_code == 200:
                pets = response.json()
                pet_ids = [str(pet[0]) for pet in pets]
                if pet_id in pet_ids:
                    break
                else:
                    print("Pet not found. Please try again.")
            else:
                print("Failed to retrieve available pets. Please try again.")

        print()
        available_dates = display_dates(pet_id)
        if available_dates:
            while True:
                chosen_date = input('Enter the date you would like to book (yyyy-mm-dd): ')
                if chosen_date in available_dates:
                    break
                else:
                    print("Date not valid or available. Please try again.")
        else:
            print("Failed to retrieve available dates.")

        print()
        display_timeslots(pet_id, chosen_date)
        timeslot = get_timeslot_choice()

        # Creating new customer or checking existing customer
        customer_id = None

        while customer_id is None:
            customer = input('\nAre you a new customer? Enter yes or no: ')
            if customer == 'yes':
                customer_name = input("Enter customer name: ")
                customer_email = input("Enter customer email: ")
                customer_id = create_customer(customer_name, customer_email)
                if customer_id:
                    rent_pet(pet_id, timeslot, customer_id, chosen_date)
                else:
                    print("Failed to create customer. Please try again.")
            elif customer == 'no':
                customer_name = input("Enter customer name: ")
                customer_email = input("Enter customer email: ")
                customer_id = query_existing_customer(customer_name, customer_email)
                if customer_id:
                    rent_pet(pet_id, timeslot, customer_id, chosen_date)
                else:
                    print("Please check the name and email and try again.")
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")

    # this is a loop for customer input

    elif adopt_pet_choice == 'adopt':
        while True:
            print()
            display_availability()
            pet_id = input('Enter the ID of the pet you would like to adopt: ')
            # This checks if the user input for pet ID is valid
            if pet_id in ['1', '2', '3']:
                adopt_pet(pet_id)
                break
            else:
                print("\nPet not found. Please try again.")
    # if the customer wants to adopt
    elif adopt_pet_choice == 'exit':

        print("Goodbye! We hope to see you again soon.")


if __name__ == '__main__':
    run()
