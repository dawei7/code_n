from typing import List


class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        modulus = 1_000_000_007
        zero = one = two = 0

        for value in nums:
            if value == 0:
                zero = (2 * zero + 1) % modulus
            elif value == 1:
                one = (2 * one + zero) % modulus
            else:
                two = (2 * two + one) % modulus

        return two
