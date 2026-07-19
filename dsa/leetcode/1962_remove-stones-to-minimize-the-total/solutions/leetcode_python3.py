import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        largest_first = [-pile for pile in piles]
        heapq.heapify(largest_first)

        for _ in range(k):
            largest = -heapq.heappop(largest_first)
            remaining = largest - largest // 2
            heapq.heappush(largest_first, -remaining)

        return -sum(largest_first)
