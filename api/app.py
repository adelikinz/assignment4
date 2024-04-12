from flask import Flask, jsonify
from db_utils import db_pethaven_overview


app = Flask(__name__)

# API endpoint to see all pets
@app.route('/pets', methods=['GET'])
def get_all_pets():
    pets = db_pethaven_overview()
    return jsonify(pets)




if __name__ == '__main__':
    app.run(debug=True, port=5004)