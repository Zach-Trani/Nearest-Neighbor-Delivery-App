import csv
import datetime
import Truck

from CreateHashTable import CreateHashMap
from Package import Package

# Read package CSV data into a list - ** NECESSARY?? ** ALSO USED IN WHILE LOOP
with open("Data/Package_Data.csv") as Package_Data_input:
    Package_Data_CSV = csv.reader(Package_Data_input)
    Package_Data_CSV = list(Package_Data_CSV)
# print(Package_Data_CSV)

# Read distance CSV data into a list
with open("Data/Distance_Data.csv") as Distance_Data_input:
    Distance_Data_CSV = csv.reader(Distance_Data_input)
    Distance_Data_CSV = list(Distance_Data_CSV)
# print(Distance_Data_CSV)

# Read address CSV data into a list
with open("Data/Address_Data.csv") as Address_Data_input:
    Address_Data_CSV = csv.reader(Address_Data_input)
    Address_Data_CSV = list(Address_Data_CSV)
print(Address_Data_CSV)


# Create package objects from the CSV package file
# Load package objects into the hash table: package_hash_table
def load_package_data(filename, package_hash_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline_time = package[5]
            pWeight = package[6]
            pStatus = "At Hub"

            # Package object
            p = Package(pID, pAddress, pDeadline_time, pCity, pZipcode, pState, pWeight, pStatus)
            
            # Insert data into hash table
            package_hash_table.insert(pID, p)

# Method for finding distance between two addresses
def distance_in_between(x_val, y_val):
    distance = Distance_Data_CSV[x_val][y_val]
    if distance == '':
        distance = Distance_Data_CSV[y_val][x_val]

    return float(distance)

# Method to get address number from string literal of address
def extract_address(address):
    for row in Address_Data_CSV:
        if address in row[2]:
            return int(row[0])

# Create truck object truck1
truck_1 = Truck.Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

# Create truck object truck2
truck_2 = Truck.Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Create truck object truck3
truck_3 = Truck.Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=5))

# instantiate the hash table
package_hash_table = CreateHashMap()

# load packages into hash table
load_package_data("Data/Package_Data.csv", package_hash_table)









# Create package objects from the CSV package file
# Load package objects into the hash table: package_hash_table
    # citing source - "C950 - Webinar 3 - Let's Go Hashing - Complete Python Code" loadMovieData function
def load_package_data(filename, package_hash_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline_time = package[5]
            pWeight = package[6]
            pStatus = "At Hub"

            # Package object
            p = Package(pID, pAddress, pDeadline_time, pCity, pZipcode, pState, pWeight, pStatus)
            
            # package insert into hash table
            package_hash_table.insert(pID, p)

# Create hash table instance
package_hash_table = CreateHashMap()

# Load Package data into hash table
load_package_data("Data/Package_Data.csv", package_hash_table)
