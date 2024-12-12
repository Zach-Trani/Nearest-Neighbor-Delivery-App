# Class for truck data - NEED TO FIX PARAMETER ORDER
class Truck:
    def __init__(self, load, package_limit, speed, mileage, departure_time, address, packages):
        self.package_limit = package_limit
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.departure_time = departure_time
        self.time = departure_time
        self.packages = packages

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (
            self.load,
            self.package_limit,
            self.speed,
            self.mileage,
            self.departure_time,
            self.address,
            self.packages
        )
