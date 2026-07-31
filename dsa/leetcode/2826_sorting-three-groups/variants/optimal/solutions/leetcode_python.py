from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        longest = [0, 0, 0]

        for value in nums:
            index = value - 1
            longest[index] = 1 + max(longest[: index + 1])

        return len(nums) - max(longest)
