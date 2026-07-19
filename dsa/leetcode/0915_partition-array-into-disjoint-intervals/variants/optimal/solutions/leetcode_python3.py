from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = nums[0]
        seen_max = nums[0]
        boundary = 0

        for index in range(1, len(nums)):
            seen_max = max(seen_max, nums[index])
            if nums[index] < left_max:
                boundary = index
                left_max = seen_max

        return boundary + 1

