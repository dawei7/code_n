from typing import List


class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        left_up = [1] * n
        left_down = [1] * n
        right_up = [1] * n
        right_down = [1] * n

        answer = 1
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                left_up[i] = left_down[i - 1] + 1
                answer = max(answer, left_up[i])
            elif nums[i - 1] > nums[i]:
                left_down[i] = left_up[i - 1] + 1
                answer = max(answer, left_down[i])

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right_up[i] = right_down[i + 1] + 1
            elif nums[i] > nums[i + 1]:
                right_down[i] = right_up[i + 1] + 1

        for removed in range(1, n - 1):
            if nums[removed - 1] < nums[removed + 1]:
                answer = max(
                    answer,
                    left_down[removed - 1] + right_down[removed + 1],
                )
            elif nums[removed - 1] > nums[removed + 1]:
                answer = max(
                    answer,
                    left_up[removed - 1] + right_up[removed + 1],
                )

        return answer
