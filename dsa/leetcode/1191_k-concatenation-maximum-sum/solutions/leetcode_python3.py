from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        modulo = 1_000_000_007

        def best_over_copies(copy_count: int) -> int:
            best = 0
            current = 0
            for _ in range(copy_count):
                for value in arr:
                    current = max(0, current + value)
                    best = max(best, current)
            return best

        if k == 1:
            return best_over_copies(1) % modulo

        best = best_over_copies(2)
        total = sum(arr)
        if total > 0:
            best += (k - 2) * total
        return best % modulo
