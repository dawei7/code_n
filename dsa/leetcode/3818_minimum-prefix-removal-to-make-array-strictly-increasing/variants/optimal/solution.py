from typing import List


class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        suffix_start = len(nums) - 1

        while suffix_start > 0 and nums[suffix_start - 1] < nums[suffix_start]:
            suffix_start -= 1

        return suffix_start
