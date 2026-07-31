from typing import List


class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        best = [1] * (k - 1) + [n]
        best_difference = n - 1
        factors = []

        def search(remaining: int, slots: int, minimum: int) -> None:
            nonlocal best, best_difference
            if slots == 1:
                if remaining >= minimum:
                    candidate = factors + [remaining]
                    difference = candidate[-1] - candidate[0]
                    if difference < best_difference:
                        best = candidate
                        best_difference = difference
                return

            factor = minimum
            while factor**slots <= remaining:
                if remaining % factor == 0:
                    factors.append(factor)
                    search(remaining // factor, slots - 1, factor)
                    factors.pop()
                factor += 1

        search(n, k, 1)
        return best
