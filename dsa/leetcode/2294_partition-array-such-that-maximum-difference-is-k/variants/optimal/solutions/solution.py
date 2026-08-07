from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        groups = 1
        minimum = nums[0]

        for value in nums[1:]:
            if value - minimum > k:
                groups += 1
                minimum = value

        return groups
