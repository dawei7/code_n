from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ordered = sorted(piles)
        return sum(ordered[len(ordered) // 3 :: 2])
