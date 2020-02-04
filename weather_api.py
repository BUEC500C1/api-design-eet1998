# Erin Thomas / U26838058 / EC 500: Building Software / Assignment 2
# Python program to find weather information for any U.S. airport using OpenWeatherMap API
# References: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask, https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

import requests
import json
import flask

# Creates Flask application server
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Erin's Weather API</h1><p>This site returns the weather information for a given United States airport.</p>"
app.run()

# Function to call OpenWeaterMap API
def api_call(city_name):
    base_url = "api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "q=" + city_name
    response = requests.get(complete_url)