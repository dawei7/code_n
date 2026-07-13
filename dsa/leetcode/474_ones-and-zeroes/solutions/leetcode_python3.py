from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        best = [[0] * (n + 1) for _ in range(m + 1)]
        for string in strs:
            zeros = string.count("0")
            ones = len(string) - zeros
            for zero_budget in range(m, zeros - 1, -1):
                for one_budget in range(n, ones - 1, -1):
                    best[zero_budget][one_budget] = max(
                        best[zero_budget][one_budget],
                        1 + best[zero_budget - zeros][one_budget - ones],
                    )
        return best[m][n]
