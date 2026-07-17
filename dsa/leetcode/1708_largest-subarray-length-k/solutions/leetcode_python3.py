from typing import List


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        start = max(range(len(nums) - k + 1), key=nums.__getitem__)
        return nums[start : start + k]
