from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will allow all origins; configure as needed


app.debug = True
countries = [
{"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
{"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
{"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.route("/countries", methods=["GET"])
def get_countries():
    return jsonify(countries)

@app.route("/countries", methods=["POST"])
def add_country():
    if request.is_json:
        my_json=request.data.decode('utf8').replace("'", '"')
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is the about page!'

@app.route('/api/page1')
def predict():
    data = {"message": "Hello from the API!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
