#
#
#
# Student Name: Joseph Byrd
# Student Id: #001081029
#
#
#

import csv
from model.HashTable import HashTable
from model.Package import Package
from model.Location import Location
from model.Truck import Truck
from model.Time import Time
import SetUp

packages = HashTable()
locations = HashTable()
distances = []


# This is the main menu that allows the user to navigate the program
def main_menu():
    stop_time = Time(8, 00)
    exit_program = False
    while not exit_program:
        print('\nWelcome to the Package delivery system\n\n'
              'Current stop time is ' + str(stop_time) +
              '\n\nPlease make a selection\n1. Enter new time\n'
              '2. Check packages at stop time\n3. Deliver all packages\n4. Exit program')
        selection = input('enter menu selection: ')

        try:
            if int(selection) == 1:
                stop_time = SetUp.get_time()
            elif int(selection) == 2:
                reset_packages()
                print('\n\n\nPackages status at ' + str(stop_time) + ':\n')
                load_and_deliver_packages(stop_time)
                for package in packages:
                    if package is not None:
                        print('Package #' + str(package[0]) + '\t' + str(package[1]))
            elif int(selection) == 3:
                reset_packages()
                print('\n\n\nPackages status at the end of the day:\n')
                mileage = "%.2f" % load_and_deliver_packages(Time(17, 0))
                for package in packages:
                    if package is not None:
                        print('Package #' + str(package[0]) + '\t' + str(package[1]))
                print('\n\nTotal miles taken is ' + mileage + ' miles')
            elif int(selection) == 4:
                exit_program = True
        except ValueError:
            print('Please make a valid selection')


# Load data into the program
def init_setup():
    global distances
    SetUp.import_addresses(locations)
    distances = SetUp.get_distances()
    SetUp.receive_packages(locations, packages)
    reset_packages()


# Resets the packages to the hub when going through the main menu
def reset_packages():
    length = len(packages)
    for x in range(0, length):
        if packages.data[x] is not None:
            packages.data[x][1].delivery_status = 'At Hub'


# Loads the packages on the trucks and delivers them. Returns the total mileage when done
def load_and_deliver_packages(s_time):
    total = 0
    truck1 = Truck(SetUp.get_packages([4, 14, 15, 16, 19, 20, 21, 34, 40], packages), Time(8, 0), False, s_time,
                   'truck 1')
    total += truck1.deliver_packages(distances)
    truck2 = Truck(SetUp.get_packages([1, 5, 6, 7, 8, 13, 25, 26, 29, 30, 31, 32, 37, 38, 39], packages), Time(9, 5),
                   False, s_time, 'truck 2')
    total += truck2.deliver_packages(distances)
    truck1 = Truck(SetUp.get_packages([10, 11, 12, 17, 22, 23, 24, 27, 28, 35], packages), Time(9, 5), True, s_time,
                   'truck 1')
    total += truck1.deliver_packages(distances)
    truck2 = Truck(SetUp.get_packages([2, 3, 9, 18, 33, 36], packages), truck2.time, True, s_time, 'truck 2')
    total += truck2.deliver_packages(distances)
    return total


# starts the program
if __name__ == '__main__':
    init_setup()
    main_menu()
