from math import gcd
from typing import List


class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)

        logarithm = [0] * (n + 1)
        for length in range(2, n + 1):
            logarithm[length] = logarithm[length // 2] + 1

        sparse_table = [nums[:]]
        power = 1
        while (1 << power) <= n:
            half = 1 << (power - 1)
            width = 1 << power
            previous = sparse_table[-1]
            sparse_table.append([gcd(previous[left], previous[left + half]) for left in range(n - width + 1)])
            power += 1

        def range_gcd(left: int, right: int) -> int:
            length = right - left + 1
            level = logarithm[length]
            width = 1 << level
            return gcd(
                sparse_table[level][left],
                sparse_table[level][right - width + 1],
            )

        def feasible(limit: int) -> bool:
            changes = 0
            last_changed = -1
            window = limit + 1

            for left in range(n - window + 1):
                if last_changed >= left:
                    continue

                right = left + limit
                if range_gcd(left, right) > 1:
                    changes += 1
                    if changes > maxC:
                        return False
                    last_changed = right

            return True

        low, high = 0, n
        while low < high:
            middle = (low + high) // 2
            if feasible(middle):
                high = middle
            else:
                low = middle + 1

        return low
