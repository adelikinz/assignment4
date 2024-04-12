from flask import Flask, jsonify, request
from db_utils import db_pethaven_overview, db_pet_id


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


if __name__ == '__main__':
    app.run(debug=True, port=5004)
