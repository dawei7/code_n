from collections import Counter
from math import isqrt
from typing import List


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        remaining = Counter(nums)
        values = list(remaining)
        neighbors = {value: [] for value in values}

        for left in values:
            for right in values:
                total = left + right
                root = isqrt(total)
                if root * root == total:
                    neighbors[left].append(right)

        def count(previous, unused):
            if unused == 0:
                return 1

            total = 0
            candidates = values if previous is None else neighbors[previous]
            for value in candidates:
                if remaining[value] == 0:
                    continue
                remaining[value] -= 1
                total += count(value, unused - 1)
                remaining[value] += 1
            return total

        return count(None, len(nums))
