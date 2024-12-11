import csv
import datetime
import Truck

from CreateHashTable import CreateHashMap
from Package import Package

# Read package CSV data into a list - might be unessacary if its being used in load package data function
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

# instantiate the hash map
package_hash_table = CreateHashMap()

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

             # Debug print - add this
            print(f"Creating package {pID}")
            
            # Insert data into hash table
            package_hash_table.insert(pID, p)
            
            # Debug print - add this
            print(f"After insertion, looking up package {pID}:")
            print(package_hash_table.lookup(pID))


load_package_data("Data/Package_Data.csv", package_hash_table)

















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

             # Debug print - add this
            print(f"Creating package {pID}")
            
            # Insert data into hash table
            package_hash_table.insert(pID, p)
            
            # Debug print - add this
            print(f"After insertion, looking up package {pID}:")
            print(package_hash_table.lookup(pID))

# Create hash table
package_hash_table = CreateHashMap()

load_package_data("Data/Package_Data.csv", package_hash_table)


# Debug print
result = package_hash_table.lookup(6)
print("Looking up package 6:")
print(result)