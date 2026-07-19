import heapq


class StockPrice:
    def __init__(self):
        self.prices: dict[int, int] = {}
        self.latest_timestamp = 0
        self.minimum_heap: list[tuple[int, int]] = []
        self.maximum_heap: list[tuple[int, int]] = []

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        heapq.heappush(self.minimum_heap, (price, timestamp))
        heapq.heappush(self.maximum_heap, (-price, timestamp))

    def current(self) -> int:
        return self.prices[self.latest_timestamp]

    def maximum(self) -> int:
        while (
            -self.maximum_heap[0][0]
            != self.prices[self.maximum_heap[0][1]]
        ):
            heapq.heappop(self.maximum_heap)
        return -self.maximum_heap[0][0]

    def minimum(self) -> int:
        while (
            self.minimum_heap[0][0]
            != self.prices[self.minimum_heap[0][1]]
        ):
            heapq.heappop(self.minimum_heap)
        return self.minimum_heap[0][0]


def solve(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    tracker: StockPrice | None = None
    output: list[int | None] = []

    for operation, args in zip(operations, arguments):
        if operation == "StockPrice":
            tracker = StockPrice()
            output.append(None)
        elif operation == "update":
            assert tracker is not None
            tracker.update(args[0], args[1])
            output.append(None)
        elif operation == "current":
            assert tracker is not None
            output.append(tracker.current())
        elif operation == "maximum":
            assert tracker is not None
            output.append(tracker.maximum())
        elif operation == "minimum":
            assert tracker is not None
            output.append(tracker.minimum())
        else:
            raise ValueError(f"unknown operation: {operation}")

    return output
