class UndergroundSystem:
    def __init__(self):
        self.active = {}
        self.routes = {}

    def checkIn(self, id, stationName, t):
        self.active[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        start_station, start_time = self.active.pop(id)
        total, count = self.routes.get((start_station, stationName), (0, 0))
        self.routes[(start_station, stationName)] = (total + t - start_time, count + 1)

    def getAverageTime(self, startStation, endStation):
        total, count = self.routes[(startStation, endStation)]
        return total / count


def solve(operations: list[tuple[str, tuple[object, ...]]]) -> list[object]:
    system = UndergroundSystem()
    outputs: list[object] = []
    for operation, arguments in operations:
        outputs.append(getattr(system, operation)(*arguments))
    return outputs
