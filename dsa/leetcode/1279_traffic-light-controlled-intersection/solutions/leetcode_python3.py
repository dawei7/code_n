from threading import Lock


class TrafficLight:
    def __init__(self):
        self.lock = Lock()
        self.green_road = 1

    def carArrived(
        self,
        carId: int,
        roadId: int,
        direction: int,
        turnGreen: "Callable[[], None]",
        crossCar: "Callable[[], None]",
    ) -> None:
        with self.lock:
            if roadId != self.green_road:
                turnGreen()
                self.green_road = roadId
            crossCar()
