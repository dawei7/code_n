from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common = set(nums[0])
        for values in nums[1:]:
            common.intersection_update(values)
        return sorted(common)
