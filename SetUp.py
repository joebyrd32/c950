import csv

import main
from model.Location import Location
from model.Package import Package
from model.Time import Time


# O(n)
# Imports packages out of csv file
def receive_packages(locations, packages):
    with open('packages.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in range(0, len(locations.data)):
                if locations.search(i) is not None:
                    if locations.search(i).address == row[1]:
                        package_id = i
            new_package = Package(package_id, row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            packages.add(int(row[0]), new_package)


# O(n^2)
# Imports distances from csv file
# noinspection PyTypeChecker
def get_distances():
    with open('distances.csv', newline='') as file:
        data = list(file)
        length = len(data)
        reader = csv.reader(data)
        distances = [[0.0] * length for i in range(length)]
        i = 0

        for row in reader:
            for x in range(0, i + 1):
                distances[i][x] = float(row[x])
                distances[x][i] = float(row[x])
            i += 1
        return distances


# O(n)
# Imports addresses from csv file
def import_addresses(locations):
    with open('locations.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            new_location = Location(row[1])
            locations.add(int(row[0]) - 1, new_location)


# O(n)
# Used to retrieve packages out of hashmap to load on truck
def get_packages(packages_numbers, packages):
    truck_packages = []
    for i in packages_numbers:
        truck_packages.append(packages.search(i))
    return truck_packages


# Used to get user input for custom time
def get_time():
    valid = False
    hour = minute = 0
    while not valid:
        try:
            hour = input('Enter a hour between 8 and 17: ')
            if int(hour) < 8 or int(hour) > 17:
                raise ValueError
            valid = True
        except ValueError:
            print('Input is not valid')

    valid = False
    while not valid:
        try:
            minute = input('Enter a hour between 0 and 59: ')
            if int(minute) < 0 or int(minute) > 59:
                raise ValueError
            valid = True
        except ValueError:
            print('Input is not valid')

    return Time(hour, minute)
