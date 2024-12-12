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
    # If the entry is empty, we can key in with x & y values reversed since matrix is symmetrical
    if distance == '':
        distance = Distance_Data_CSV[y_val][x_val]

    return float(distance)

# Method to get address number from string literal of address
def extract_address(address):
    for row in Address_Data_CSV:
        if address in row[2]:
            return int(row[0])


# *-- manually iterate package placement, split conflicting Nearest Neighbor constraints amongst the 3 trucks --*
# Create truck object truck1 - packages needing to leave early
truck_1 = Truck.Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

# Create truck object truck2 - packages delayed until 9:00am
truck_2 = Truck.Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Create truck object truck3 - packages with wrong address & other packages. Will update departure_time before calling the optimization
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


# Nearest Neighbor algo
    # Takes in a truck obj
    # calculates next closest address based on current
    # records route mileage
    # records time packages are delivered

def deliver_packages(truck):
    # Loop through package ID's & temporarily store package objects in not_delivered list
    need_to_deliver = []
    for packageID in truck.packages: # (hash map keys)
        package = package_hash_table.lookup(packageID) # retrieve package object (hash map values) and store into not_delivered
        need_to_deliver.append(package)
    # Clear the unordered package list so they can be re-ordered using nearest neighbor algorithm
    truck.packages.clear()

    while len(need_to_deliver) > 0:
        next_address = 140 # arbitrarily set as it will be rewriteen (140 is max dist for a truck)
        next_package = None

        for package in need_to_deliver:
            # Retrieve matrix coordinates
            x_index = extract_address(truck.address)
            y_index = extract_address(package.address)
            distance_diff = distance_in_between(x_index, y_index)

            if distance_diff <= next_address:
                next_address = distance_diff
                next_package = package

        # add the next closest package to our final list
        truck.packages.append(next_package.ID)
        need_to_deliver.remove(next_package) # remove off to do list
        truck.mileage += next_address # sum of address to address distances
        truck.address = next_package.address # reset our reference address
        truck.time += datetime.timedelta(hours=next_address/18) # miles / 18 mph= hour, then use datetime to convert to minutes
        next_package.delivery_time = truck.time 
        next_package.departure_time = truck.departure_time

# Call Nearest Neighbor algo for each truck
deliver_packages(truck_1)
deliver_packages(truck_2)
truck_3.departure_time = min(truck_1.time, truck_2.time)
deliver_packages(truck_3)


    # # Put the trucks through the loading process
        # delivering_packages(truck1)
        # delivering_packages(truck2)

      # Need to add some logic that departs the 3rd truck after a driver frees up
        # delivering_packages(truck3)