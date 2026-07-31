from heapq import heappush, heapreplace


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
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


def solve(k: int, nums: list[int], stream: list[int]) -> list[int]:
    kth_largest = KthLargest(k, nums)
    return [kth_largest.add(value) for value in stream]
