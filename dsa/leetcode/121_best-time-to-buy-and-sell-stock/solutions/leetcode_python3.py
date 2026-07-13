from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        lowest = float("inf")
        for price in prices:
            lowest = min(lowest, price)
            best = max(best, price - lowest)
        return best
