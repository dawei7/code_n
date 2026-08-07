from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        factor_mask = [0, 0, 1, 2, 1, 4, 3, 8, 1, 2, 5]
        left = 0
        used_factors = 0
        answer = 2

        for right, value in enumerate(nums):
            mask = factor_mask[value]
            while used_factors & mask:
                used_factors ^= factor_mask[nums[left]]
                left += 1
            used_factors |= mask
            answer = max(answer, right - left + 1)

        return answer
