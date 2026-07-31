from threading import Lock


class TrafficLight:
    def __init__(self):
        self.lock = Lock()
        self.green_road = 1

    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        with self.lock:
            if roadId != self.green_road:
                turnGreen()
                self.green_road = roadId
            crossCar()
