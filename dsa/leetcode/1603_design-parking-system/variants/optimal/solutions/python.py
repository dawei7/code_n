class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.available = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.available[carType] == 0:
            return False
        self.available[carType] -= 1
        return True


def solve(big: int, medium: int, small: int, carTypes: list[int]) -> list[bool]:
    parking = ParkingSystem(big, medium, small)
    return [parking.addCar(car_type) for car_type in carTypes]
