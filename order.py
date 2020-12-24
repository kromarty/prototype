from vehicle import vehicle

class order:
    def __init__(self):
        self.vehicles = []
        self.address = None

    def AddVehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def SetDeliveryAddress(self, address):
        self.address = address

    def Cost(self):
        n = 0
        for i in self.vehicles:
            n += i.price
        return n