from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        answer = abs(nums[0] - nums[-1])
        for index in range(1, len(nums)):
            answer = max(answer, abs(nums[index] - nums[index - 1]))
        return answer
