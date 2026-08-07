from typing import List


class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        n = len(usageLimits)
        frequencies = [0] * (n + 1)

        for limit in usageLimits:
            frequencies[min(limit, n)] += 1

        available = 0
        groups = 0

        for limit in range(1, n + 1):
            for _ in range(frequencies[limit]):
                available += limit
                required = (groups + 1) * (groups + 2) // 2
                if available >= required:
                    groups += 1

        return groups
