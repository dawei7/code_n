from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        descents = 0
        for index, value in enumerate(nums):
            if value > nums[(index + 1) % len(nums)]:
                descents += 1
                if descents > 1:
                    return False
        return True
