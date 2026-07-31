class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.available = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.available[carType] == 0:
            return False
        self.available[carType] -= 1
        return True
