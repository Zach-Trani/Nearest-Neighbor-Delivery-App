class Package:
    def __init__(self, ID, address, city, state, zip_code, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        return (
            f"Package ID       : {self.ID}\n"
            f"Address          : {self.address}\n"
            f"City             : {self.city}\n"
            f"State            : {self.state}\n"
            f"ZIP Code         : {self.zip_code}\n"
            f"Deadline         : {self.deadline}\n"
            f"Weight           : {self.weight} lbs\n"
            f"Status           : {self.status}\n"
            f"Delivery Time    : {self.delivery_time}"
        )