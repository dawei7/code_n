from functools import cache
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        values = tuple(sorted(nums, reverse=True))
        if values[0] > target:
            return False

        full_mask = (1 << len(values)) - 1

        @cache
        def search(mask: int, remainder: int) -> bool:
            if mask == full_mask:
                return remainder == 0

            for index, value in enumerate(values):
                if mask & (1 << index) or remainder + value > target:
                    continue
                if search(
                    mask | (1 << index),
                    (remainder + value) % target,
                ):
                    return True
            return False

        return search(0, 0)
