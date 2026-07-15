"""Source-native synchronization reference for LeetCode 1279."""

from threading import Lock


class TrafficLight:
    def __init__(self):
        self._lock = Lock()
        self._green_road = 1

    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        with self._lock:
            if roadId != self._green_road:
                turnGreen()
                self._green_road = roadId
            crossCar()
