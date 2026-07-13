from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for value in nums:
            ones = (ones ^ value) & ~twos
            twos = (twos ^ value) & ~ones
        return ones
