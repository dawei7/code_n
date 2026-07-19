import heapq


class StockPrice:
    def __init__(self):
        self.prices = {}
        self.latest_timestamp = 0
        self.minimum_heap = []
        self.maximum_heap = []

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
