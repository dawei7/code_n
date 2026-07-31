from collections import deque
from typing import List


class RideSharingSystem:
    def __init__(self) -> None:
        self.riders: deque[int] = deque()
        self.drivers: deque[int] = deque()
        self.active_riders: set[int] = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.active_riders.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.riders and self.riders[0] not in self.active_riders:
            self.riders.popleft()

        if not self.riders or not self.drivers:
            return [-1, -1]

        rider_id = self.riders.popleft()
        driver_id = self.drivers.popleft()
        self.active_riders.remove(rider_id)
        return [driver_id, rider_id]

    def cancelRider(self, riderId: int) -> None:
        self.active_riders.discard(riderId)


def solve(operations: List[str], arguments: List[List[int]]) -> List[object]:
    system: RideSharingSystem | None = None
    output: List[object] = []

    for operation, values in zip(operations, arguments):
        if operation == "RideSharingSystem":
            system = RideSharingSystem()
            output.append(None)
        elif operation == "addRider":
            assert system is not None
            system.addRider(values[0])
            output.append(None)
        elif operation == "addDriver":
            assert system is not None
            system.addDriver(values[0])
            output.append(None)
        elif operation == "matchDriverWithRider":
            assert system is not None
            output.append(system.matchDriverWithRider())
        elif operation == "cancelRider":
            assert system is not None
            system.cancelRider(values[0])
            output.append(None)
        else:
            raise ValueError(f"unknown operation: {operation}")

    return output
