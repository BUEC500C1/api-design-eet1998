# Weather App
The purpose of this is to design an API to get the weather conditions for a specific airport in the United States.

## Summary
This code calls the API from openweathermap.org and uses it to get the weather information for any city or airport location. If the user inputs a city, the function ```api_call``` converts the JSON formatted data from the API to Python format and outputs the current temperature, pressure, and humidity levels as well as a general weather description. If the user inputs an airport, the function ```find_city``` retrieves the city of any inputted airport by iterating through a .csv file and passes this result to the ```api_call``` function.

### User Stories
- As a parent, I would like to know the weather of the city where my child lives.
- As a traveller, I would like to know the weather where my airport I am arriving.
- As a weather enthusiast, I would like to know the weather of random places, just for fun.

## How to Run This Code
1. Clone this repository: ```git clone https://github.com/BUEC500C1/api-design-eet1998.git```.
2. Fire up your local terminal and run ```python weather_api.py```.
3. Reap the benefits of knowing the weather information at the city and/or airport of your choosing.

## References
- https://stackoverflow.com/questions/17432478/python-print-to-one-line-with-time-delay-between-prints?rq=1
- https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
- https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
- https://realpython.com/python-keyerror/ 
- https://docs.python.org/3.4/library/csv.html?highlight=csv
