from typing import List


class Solution:
    def maxScore(self, prices: List[int]) -> int:
        totals = {}
        for index, price in enumerate(prices):
            key = price - index
            totals[key] = totals.get(key, 0) + price
        return max(totals.values())
