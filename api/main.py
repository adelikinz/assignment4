import requests
import json

# Function to get available pets from the API
def get_available_pets():
    result = requests.get(
        'http://127.0.0.1:5004/pets',
        headers={'content-type': 'application/json'}
    )
    return result.json()  # Extract the 'pets' key from the JSON response

# Function to book a pet for adoption
def adopt_pet(pet_id, customer_name):
    adoption = {
        "pet_id": pet_id,
        "customer_name": customer_name,
    }
    result = requests.put(
        'http://127.0.0.1:5004/adopt_pet',
        headers={'content-type': 'application/json'},
        data=json.dumps(adoption)
    )
    print("Response content:", result.content)  # Print response content for debugging
    return result.json()


# Function to display available pets
def display_available_pets(pets):
    print("{:<10} {:<15} {:<15} {:<15} {:<10}".format('Pet ID', 'Pet Name', 'Pet Type', 'Age', 'Available'))
    print('-' * 70)

    for pet in pets:
        print(pet[0], pet[1], pet[2], pet[3], "Yes" if pet[4] else "No")


# Main function to run the application
def run():
    print('############################')
    print('Welcome to Pet Haven!')
    print('############################')
    print()

    available_pets = get_available_pets()
    print('Available Pets', available_pets)  #####
    print('####### AVAILABLE PETS #######')
    print()
    display_available_pets(available_pets)
    print()

    adopt_pet_choice = input('Would you like to adopt a pet (y/n)? ')
    if adopt_pet_choice.lower() == 'y':
        pet_id = input('Enter the ID of the pet you would like to adopt: ')
        customer_name = input('Please enter your name: ')
        adoption_result = adopt_pet(pet_id, customer_name)
        if 'error' in adoption_result:
            print("Error:", adoption_result['error'])
        else:
            print("Adoption successful! Thank you for adopting", adoption_result['pet_name'])
    print()
    print('Thank you for using Pet Haven!')


# Execute the run function if the script is run directly
if __name__ == '__main__':
    run()