import heapq
from math import isqrt


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            richest = -heapq.heappop(heap)
            heapq.heappush(heap, -isqrt(richest))

        return -sum(heap)
