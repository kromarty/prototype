import numpy as np
class warehouse:
    def __init__(self):
        try:
            self.vehicles = np.load('database.npy', allow_pickle=True).item()
        except FileNotFoundError:
            self.vehicles = {}
        try:
            self.places = list(np.load('places.npy', allow_pickle=True))
        except FileNotFoundError:
            self.places = list(range(10))