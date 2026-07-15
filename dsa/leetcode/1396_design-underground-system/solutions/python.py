"""Optimal app-local solution for LeetCode 1396."""


class UndergroundSystem:
    def __init__(self):
        self.active: dict[int, tuple[str, int]] = {}
        self.routes: dict[tuple[str, str], list[int]] = {}

    def checkIn(self, passenger_id: int, station_name: str, time: int) -> None:
        self.active[passenger_id] = (station_name, time)

    def checkOut(self, passenger_id: int, station_name: str, time: int) -> None:
        start_station, start_time = self.active.pop(passenger_id)
        aggregate = self.routes.setdefault((start_station, station_name), [0, 0])
        aggregate[0] += time - start_time
        aggregate[1] += 1

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        total, count = self.routes[(start_station, end_station)]
        return total / count


def solve(operations: list[tuple[str, tuple[object, ...]]]) -> list[object]:
    system = UndergroundSystem()
    outputs: list[object] = []
    for operation, arguments in operations:
        outputs.append(getattr(system, operation)(*arguments))
    return outputs
