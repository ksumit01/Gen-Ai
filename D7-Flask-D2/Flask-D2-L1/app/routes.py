# app/routes.py
import os
import json
from flask import Flask, jsonify, request,render_template

app = Flask(__name__)

debug = True

# Function to load weather data from JSON file
def load_weather_data():
    data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'weather_data.json')
    print(data_file)
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    else:
        return {}  # Return an empty dictionary if the file is empty or doesn't exist

# Function to save weather data to JSON file
def save_weather_data(data):
    data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'weather_data.json')
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

# ... (previous code)

@app.route('/', methods=['GET'])
def index():
    weather_data = load_weather_data()  # Load weather data from the JSON file
    return render_template('index.html', weather_data=weather_data)
@app.route('/weather/<string:city>/', methods=['GET'])  # Added GET method route
def get_weather(city):
    weather_data = load_weather_data()
    if city in weather_data:
        return jsonify({'city': city, **weather_data[city]})
    else:
        return 'City Not Found', 404
@app.route('/add_weather/', methods=['POST'])
def add_weather():
    data = request.form
    city = data.get('city')
    if city:
        weather_data = load_weather_data()
        if city in weather_data:
            return jsonify({'status': 'error', 'message': 'City already exists'}), 400
        temperature = data.get('temperature')
        weather = data.get('weather')
        weather_data[city] = {'temperature': temperature, 'weather': weather}
        save_weather_data(weather_data)
        return jsonify({'status': 'success', 'message': 'Data added successfully'}), 201
    return jsonify({'status': 'error', 'message': 'Data not added'}), 400


# Add the POST endpoint for updating weather data

@app.route('/update_weather/', methods=['POST'])
def update_weather():
    data = request.form
    city = data.get('city')
    if city:
        weather_data = load_weather_data()
        if city not in weather_data:
            return jsonify({'status': 'error', 'message': 'City not found'}), 404
        temperature = data.get('temperature')
        weather = data.get('weather')
        weather_data[city] = {'temperature': temperature, 'weather': weather}
        save_weather_data(weather_data)
        return jsonify({'status': 'success', 'message': 'Data updated successfully'}), 200
    return jsonify({'status': 'error', 'message': 'Data not updated'}), 400


# Add the GET endpoint for deleting weather data
@app.route('/delete_weather/<string:city>/', methods=['DELETE'])  # Updated route to include the city parameter
def delete_weather(city):
    weather_data = load_weather_data()
    if city in weather_data:
        del weather_data[city]
        save_weather_data(weather_data)
        return '', 204  # Return 204 No Content on successful deletion
    else:
        return 'City Not Found', 404



if __name__ == '__main__':
    app.run()
