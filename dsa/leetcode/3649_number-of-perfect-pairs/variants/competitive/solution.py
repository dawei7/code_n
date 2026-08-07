from typing import List


class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        magnitudes = sorted(abs(value) for value in nums)
        answer = 0
        left = 0

        for right, magnitude in enumerate(magnitudes):
            while magnitude > 2 * magnitudes[left]:
                left += 1
            answer += right - left

        return answer
