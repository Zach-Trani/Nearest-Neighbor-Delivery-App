import csv
import datetime

from CreateHashTable import CreateHashMap
from Package import Package

# Read the file of package information
with open("Data/Package_Data.csv") as csvfile2:
    CSV_Package = csv.reader(csvfile2)
    CSV_Package = list(CSV_Package)


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
            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline_time, pWeight, pStatus)

            # Insert data into hash table
            package_hash_table.insert(pID, p)

# Create hash table
package_hash_table = CreateHashMap()

load_package_data("CSV/Package_File.csv", package_hash_table)


Class Main:

    # lets log the first id from our hash table

    # something along the lines of 
    print(package_hash_table.lookup(0))