# Reference: https://www.programiz.com/python-programming/reading-csv-files
import csv

# Iterates through all rows in the .csv file and returns city for airport input
def find_city(airport):
    with open("airports.csv", 'r') as file:
        csv_file = csv.DictReader(file)
        # Iterates through all rows in .csv file and returns municipality for given input airport
        for row in csv_file:
            if row[3] == airport:
                return row[10]

    return


