from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will allow all origins; configure as needed

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/page1')
def predict():
    data = {"message": "Hello from the API!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
