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
