# Erin Thomas / U26838058 / EC 500: Building Software / Assignment 2
# Python program to find weather information for any U.S. airport using OpenWeatherMap API
# References: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask, https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/, https://realpython.com/python-keyerror/ 

import requests
import json
import flask
from time import sleep
from flask import jsonify
from flask import request
from find_city import find_city

# Creates Flask application server
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#@app.route('/', methods=['GET'])
#def home():
    #return "<h1>Erin's Weather API</h1><p>This site returns the weather information for a given United States airport.</p>"
#app.run()

# API key received from openweathermap.org 
api_key = 'd9c3071452f6c3314a2576e2e82f3354'

# Function to call OpenWeaterMap API
def api_call(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="
    complete_url = base_url + city + "&appid=" + api_key
    response = requests.get(complete_url)
    # Converts data from JSON to Python format
    x = response.json()

    if x["cod"] != "404":
        
        current_temperature = x["main"]["temp"]
        current_pressure = x["main"]["pressure"]
        current_humidity = x["main"]["humidity"]
        weather_description = x["weather"][0]["description"]

        print("Temperature: " + str(current_temperature)) + " K")
        print("Atmospheric Pressure: " + str(current_pressure) + " hPa")
        print("Humidity: " + str(current_humidity)+ " %")
        print("Weather Description: " + str(weather_description))
    
    else:
        print("Error!")

# Main function to receive user input and make appropriate function calls
def main():
    print("Hello. Welcome to my weather app.") ; sleep(1.0)

    while True:
        user_choice = input("Would you like to receive the weather at a city or an airport? Enter C for city and A for airport (or enter Q to quit): ")
        # Error check user input
        if (user_choice != "C") & (user_choice != "A") & (user_choice!= "Q"):
            print("Error: Please enter either C for city or A for airport.")
        if user_choice == "C":
            city = input("Please enter a city name: ")
            api_call(city)
            print()
        if user_choice == "A":
            airport = input("Please enter an airport name: ")
            municipality = find_city(airport)
            api_call(municipality)
            print()
        if user_choice == "Q":
            sleep(1.0)
            print("Goodbye.")
            break

if __name__ == '__main__':
    main()
    