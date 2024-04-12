import requests


# Function to get available pets from the API
def get_available_pets():
    result = requests.get(
        'http://127.0.0.1:5004/pets',
        headers={'content-type': 'application/json'}
    )
    return result


# Function to get pet by its id from the API
def get_pet_id(pet_id):
    result = requests.get(
        'http://127.0.0.1:5004/pets/{}'.format(pet_id),
        headers={'content-type': 'application/json'}
    )
    return result.json()


# Main function to run the application - please amend as you feel fit
def run():
    print('############################')
    print('Welcome to Pet Haven!')
    print('############################')
    print()

    available_pets = get_available_pets()
    print('Available Pets', available_pets)
    print('####### AVAILABLE PETS #######')
    print()

    adopt_pet_choice = input('Would you like to adopt a pet (y/n)? ')
    if adopt_pet_choice.lower() == 'y':
        input('Enter the ID of the pet you would like to adopt: ')
        input('Please enter your name: ')
    else:
        print("Adoption successful! Thank you for adopting", ['pet_name'])
    print()
    print('Thank you for using Pet Haven!')


# Execute the run function if the script is run directly
if __name__ == '__main__':
    run()
