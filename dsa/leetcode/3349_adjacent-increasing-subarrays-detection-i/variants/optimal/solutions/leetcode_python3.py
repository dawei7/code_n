from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        previous_run = 0
        current_run = 1

        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                current_run += 1
            else:
                previous_run = current_run
                current_run = 1

            if current_run // 2 >= k or min(previous_run, current_run) >= k:
                return True

        return False
