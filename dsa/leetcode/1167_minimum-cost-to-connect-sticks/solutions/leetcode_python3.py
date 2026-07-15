from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        total = 0
        while len(sticks) > 1:
            combined = heappop(sticks) + heappop(sticks)
            total += combined
            heappush(sticks, combined)
        return total
