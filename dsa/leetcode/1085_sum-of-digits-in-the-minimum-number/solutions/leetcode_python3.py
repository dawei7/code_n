from typing import List


class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        value = min(nums)
        digit_sum = 0
        while value:
            digit_sum += value % 10
            value //= 10
        return int(digit_sum % 2 == 0)
