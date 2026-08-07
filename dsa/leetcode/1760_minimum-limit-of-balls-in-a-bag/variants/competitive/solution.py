from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low = 1
        high = max(nums)

        while low < high:
            penalty = (low + high) // 2
            required = sum((balls - 1) // penalty for balls in nums)

            if required <= maxOperations:
                high = penalty
            else:
                low = penalty + 1

        return low
