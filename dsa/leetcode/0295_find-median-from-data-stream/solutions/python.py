"""Two-heap solution for LeetCode 295: Find Median from Data Stream."""

import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.lower: list[int] = []
        self.upper: list[int] = []

    def add_num(self, value: int) -> None:
        if not self.lower or value <= -self.lower[0]:
            heapq.heappush(self.lower, -value)
        else:
            heapq.heappush(self.upper, value)

        if len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        elif len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def median(self) -> float:
        if len(self.lower) > len(self.upper):
            return float(-self.lower[0])
        return (-self.lower[0] + self.upper[0]) / 2.0


def solve(stream: list[int]) -> list[float]:
    finder = MedianFinder()
    result: list[float] = []
    for value in stream:
        finder.add_num(value)
        result.append(finder.median())
    return result
