# tests/test_routes.py
import os
import json
import unittest
from flask import Flask
from app.routes import app, load_weather_data, save_weather_data

class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.testing = True  # Set the app to testing mode
        self.app = app.test_client()
        # Initialize the JSON file with test data
        test_data = {
            'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
            'New York': {'temperature': 20, 'weather': 'Sunny'}
        }
        data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'weather_data.json')
        with open(data_file, 'w') as file:
            json.dump(test_data, file, indent=4)




    def test_get_weather(self):
        response = self.app.get('/weather/San Francisco/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['city'], 'San Francisco')
        self.assertEqual(data['temperature'], 14)
        self.assertEqual(data['weather'], 'Cloudy')

    def test_get_weather_city_not_found(self):
        response = self.app.get('/weather/NonExistentCity/')
        self.assertEqual(response.status_code, 404)

    def test_create_weather(self):
        new_data = {
            'city': 'Chicago',
            'temperature': 65,
            'weather': 'Partly Cloudy'  # Corrected spelling from 'conditions'
        }
        response = self.app.post('/add_weather/', data=new_data)
        self.assertEqual(response.status_code, 201)  # 201 Created

        # Verify that the data is created and can be retrieved
        response = self.app.get('/weather/Chicago/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['city'], 'Chicago')
        self.assertEqual(int(data['temperature']), 65)  # Convert temperature to int

    def test_update_weather(self):
        updated_data = {
            'city': 'New York',  # Specify the city to update
            'temperature': 75,
            'weather': 'Sunny'  # Corrected spelling from 'conditions'
        }
        response = self.app.post('/update_weather/', data=updated_data)
        self.assertEqual(response.status_code, 200)

        # Verify that the data is updated
        response = self.app.get('/weather/New York/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(int(data['temperature']), 75)  # Convert temperature to int

    def test_delete_weather(self):
        response = self.app.delete('/delete_weather/San Francisco/')
        self.assertEqual(response.status_code, 204)  # 204 No Content

        # Verify that the data is deleted
        response = self.app.get('/weather/San Francisco/')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
