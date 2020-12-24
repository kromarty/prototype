from vehicle import vehicle

class supply:
    def __init__(self, provider):
        self.provider = provider
        self.vehicles = []

    def AddVehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def GetProducts(self):
        for v in self.vehicles:
            v.get_info()