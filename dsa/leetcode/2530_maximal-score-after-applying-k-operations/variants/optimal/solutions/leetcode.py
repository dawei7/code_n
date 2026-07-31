from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-value for value in nums]
        heapify(heap)
        score = 0

        for _ in range(k):
            value = -heappop(heap)
            score += value
            heappush(heap, -((value + 2) // 3))

        return score
