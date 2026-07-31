from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0

        for number in nums:
            largest_digit = 0
            repeated_ones = 0

            while number:
                largest_digit = max(largest_digit, number % 10)
                repeated_ones = repeated_ones * 10 + 1
                number //= 10

            total += largest_digit * repeated_ones

        return total
