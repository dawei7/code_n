from heapq import heappush, heapreplace
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for value in nums:
            self._offer(value)

    def _offer(self, value: int) -> None:
        if len(self.heap) < self.k:
            heappush(self.heap, value)
        elif value > self.heap[0]:
            heapreplace(self.heap, value)

    def add(self, val: int) -> int:
        self._offer(val)
        return self.heap[0]
