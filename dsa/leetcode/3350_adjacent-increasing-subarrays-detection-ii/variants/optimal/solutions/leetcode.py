from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        previous_run = 0
        current_run = 1
        answer = 0

        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                current_run += 1
            else:
                previous_run = current_run
                current_run = 1

            answer = max(
                answer,
                current_run // 2,
                min(previous_run, current_run),
            )

        return answer
