from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        modulus = 1_000_000_007
        nums.sort()

        powers = [1] * (len(nums) + 1)
        for exponent in range(1, len(powers)):
            powers[exponent] = (powers[exponent - 1] * 2) % modulus

        left = 0
        right = len(nums) - 1
        answer = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                answer = (answer + powers[right - left]) % modulus
                left += 1
            else:
                right -= 1

        return answer
