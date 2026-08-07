from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        prefix_sum = 0
        answer = -1

        for side in sorted(nums):
            if prefix_sum > side:
                answer = prefix_sum + side
            prefix_sum += side

        return answer
