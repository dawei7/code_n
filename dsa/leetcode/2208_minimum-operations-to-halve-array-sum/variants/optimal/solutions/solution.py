import heapq
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = [-float(value) for value in nums]
        heapq.heapify(heap)
        target = sum(nums) / 2
        reduction = 0.0
        operations = 0

        while reduction < target:
            largest = -heapq.heappop(heap)
            half = largest / 2
            reduction += half
            operations += 1
            heapq.heappush(heap, -half)

        return operations
