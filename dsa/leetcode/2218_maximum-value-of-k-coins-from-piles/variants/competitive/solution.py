from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        impossible = -(10**30)
        best = [0] + [impossible] * k
        for pile in piles:
            updated = best[:]
            prefix = 0
            for taken, value in enumerate(pile[:k], start=1):
                prefix += value
                for previous in range(k - taken + 1):
                    updated[previous + taken] = max(updated[previous + taken], best[previous] + prefix)
            best = updated
        return best[k]
