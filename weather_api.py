# Erin Thomas / U26838058 / EC 500: Building Software / Assignment 2
# Python program to find weather information for any U.S. airport using OpenWeatherMap API
# References: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask, https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

import requests
import json
import flask
from find_csv import find_city

# Creates Flask application server
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Erin's Weather API</h1><p>This site returns the weather information for a given United States airport.</p>"
app.run()

# Function to call OpenWeaterMap API
def api_call(city):
    base_url = "api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "q=" + city_name
    response = requests.get(complete_url)
    # Converts data from JSON to Python format
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

# Main function to receive user input and make appropriate function calls
def main():
    user_choice = input("Would you like to receive the weather at a city or an airport? Enter C for city and A for airport:")
    if user_choice == "C":
        city = input("Please enter a city name:")
        api_call(city)
        print()
    if user_choice == "A":
        airport = input("Please enter an airport name:")
        find_city(airport)
        print()

if __name__ == '__main__':
    main()
    