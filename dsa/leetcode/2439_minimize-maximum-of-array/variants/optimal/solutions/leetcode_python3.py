from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        answer = 0

        for index, value in enumerate(nums):
            prefix_sum += value
            answer = max(answer, (prefix_sum + index) // (index + 1))

        return answer
