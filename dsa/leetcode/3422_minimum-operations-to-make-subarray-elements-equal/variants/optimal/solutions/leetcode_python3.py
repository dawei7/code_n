from collections import Counter
from heapq import heappop, heappush
from typing import List


class _SlidingMedian:
    def __init__(self) -> None:
        self.lower = []
        self.upper = []
        self.removed = Counter()
        self.lower_size = 0
        self.upper_size = 0
        self.lower_sum = 0
        self.upper_sum = 0

    def _prune(self, heap: List[int], sign: int) -> None:
        while heap:
            value = sign * heap[0]
            if self.removed[value] == 0:
                break
            self.removed[value] -= 1
            heappop(heap)

    def _balance(self) -> None:
        if self.lower_size > self.upper_size + 1:
            value = -heappop(self.lower)
            self.lower_size -= 1
            self.lower_sum -= value
            self.upper_size += 1
            self.upper_sum += value
            heappush(self.upper, value)
            self._prune(self.lower, -1)
        elif self.lower_size < self.upper_size:
            value = heappop(self.upper)
            self.upper_size -= 1
            self.upper_sum -= value
            self.lower_size += 1
            self.lower_sum += value
            heappush(self.lower, -value)
            self._prune(self.upper, 1)

    def add(self, value: int) -> None:
        if not self.lower or value <= -self.lower[0]:
            heappush(self.lower, -value)
            self.lower_size += 1
            self.lower_sum += value
        else:
            heappush(self.upper, value)
            self.upper_size += 1
            self.upper_sum += value
        self._balance()

    def discard(self, value: int) -> None:
        self.removed[value] += 1
        if value <= -self.lower[0]:
            self.lower_size -= 1
            self.lower_sum -= value
            if value == -self.lower[0]:
                self._prune(self.lower, -1)
        else:
            self.upper_size -= 1
            self.upper_sum -= value
            if self.upper and value == self.upper[0]:
                self._prune(self.upper, 1)
        self._balance()

    def cost(self) -> int:
        median = -self.lower[0]
        return (
            median * self.lower_size
            - self.lower_sum
            + self.upper_sum
            - median * self.upper_size
        )


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        window = _SlidingMedian()
        for value in nums[:k]:
            window.add(value)

        answer = window.cost()
        for right in range(k, len(nums)):
            window.add(nums[right])
            window.discard(nums[right - k])
            answer = min(answer, window.cost())

        return answer
