from typing import List

class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        lock_count = len(strength)
        full_mask = (1 << lock_count) - 1
        best = [10**18] * (full_mask + 1)
        best[0] = 0

        for mask in range(full_mask + 1):
            broken = mask.bit_count()
            factor = 1 + broken * k

            for index, required in enumerate(strength):
                if mask & (1 << index):
                    continue

                minutes = (required + factor - 1) // factor
                next_mask = mask | (1 << index)
                best[next_mask] = min(best[next_mask], best[mask] + minutes)

        return best[full_mask]
