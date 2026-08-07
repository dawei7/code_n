from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left < right:
            divisor = (left + right) // 2
            rounded_sum = sum((value + divisor - 1) // divisor for value in nums)
            if rounded_sum <= threshold:
                right = divisor
            else:
                left = divisor + 1

        return left
