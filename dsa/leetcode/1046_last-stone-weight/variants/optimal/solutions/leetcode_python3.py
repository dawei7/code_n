from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapify(heap)

        while len(heap) > 1:
            heaviest = -heappop(heap)
            second_heaviest = -heappop(heap)
            if heaviest != second_heaviest:
                heappush(heap, -(heaviest - second_heaviest))

        return -heap[0] if heap else 0

