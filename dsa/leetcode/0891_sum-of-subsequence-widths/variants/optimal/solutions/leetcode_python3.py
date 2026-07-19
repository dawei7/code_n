from typing import List


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        modulus = 1_000_000_007
        ordered = sorted(nums)
        answer = 0
        power = 1

        for index, value in enumerate(ordered):
            answer += (value - ordered[-1 - index]) * power
            power = power * 2 % modulus

        return answer % modulus
