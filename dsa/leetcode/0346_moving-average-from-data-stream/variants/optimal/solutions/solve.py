from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.total = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.total += val
        if len(self.window) > self.size:
            self.total -= self.window.popleft()
        return self.total / len(self.window)


def solve(size: int, stream: list[int]) -> list[float]:
    moving_average = MovingAverage(size)
    return [moving_average.next(value) for value in stream]
