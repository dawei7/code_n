from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        increments = sum(value.bit_count() for value in nums)
        doubles = max(0, max(nums).bit_length() - 1)
        return increments + doubles
