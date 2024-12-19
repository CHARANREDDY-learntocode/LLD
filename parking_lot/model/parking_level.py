from abc import abstractmethod

from torch.utils.hipify.hipify_python import value


class ParkingLevel:
    def __init__(self, total_spots, spot_type):
        self.total_spots = total_spots
        self.occupied_spots = {}
        self.spot_type = spot_type

    def park(self, vehicle):
        if self.spot_type != vehicle.type:
            raise ValueError()
        if len(self.occupied_spots) == self.total_spots:
            raise ValueError()
        self.occupied_spots[vehicle.id] = vehicle

    def un_park(self, vehicle):
        if vehicle.id not in self.occupied_spots:
            raise ValueError()
        self.occupied_spots.pop(vehicle.id)

