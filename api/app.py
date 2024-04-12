from flask import Flask, jsonify, request
from db_utils import db_pethaven_overview


app = Flask(__name__)

# API endpoint to see all pets
@app.route('/pets', methods=['GET'])
def get_all_pets():
    pets = db_pethaven_overview()
    return jsonify(pets)

    # API endpoint to adopt a pet
@app.route('/adopt_pet', methods=['POST'])
def adopt_pet():
    data = request.json
    pet_id = data.get('pet_id')
    customer_name = data.get('customer_name')


if __name__ == '__main__':
    app.run(debug=True, port=5004)