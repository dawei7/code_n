from heapq import nlargest, nsmallest
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        smallest = nsmallest(4, nums)
        largest = sorted(nlargest(4, nums))
        return min(high - low for low, high in zip(smallest, largest))
