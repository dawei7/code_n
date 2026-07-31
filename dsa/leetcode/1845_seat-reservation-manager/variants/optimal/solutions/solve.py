"""App-local reference solution for LeetCode 1845."""

import heapq


class SeatManager:
    def __init__(self, n: int):
        self.next_seat = 1
        self.released: list[int] = []

    def reserve(self) -> int:
        if self.released:
            return heapq.heappop(self.released)
        seat = self.next_seat
        self.next_seat += 1
        return seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.released, seatNumber)


def solve(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    manager: SeatManager | None = None
    output: list[int | None] = []
    for operation, args in zip(operations, arguments):
        if operation == "SeatManager":
            manager = SeatManager(args[0])
            output.append(None)
        elif operation == "reserve":
            assert manager is not None
            output.append(manager.reserve())
        elif operation == "unreserve":
            assert manager is not None
            manager.unreserve(args[0])
            output.append(None)
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output
