class UndergroundSystem:
    def __init__(self):
        self.active = {}
        self.routes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.active[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.active.pop(id)
        total, count = self.routes.get((start_station, stationName), (0, 0))
        self.routes[(start_station, stationName)] = (total + t - start_time, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.routes[(startStation, endStation)]
        return total / count
