from math import isqrt
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for value in nums:
            divisor_sum = 1 + value
            interior_pairs = 0

            for divisor in range(2, isqrt(value) + 1):
                if value % divisor != 0:
                    continue

                other = value // divisor
                if divisor == other:
                    interior_pairs = 2
                    break

                interior_pairs += 1
                if interior_pairs > 1:
                    break
                divisor_sum += divisor + other

            if interior_pairs == 1:
                total += divisor_sum

        return total
