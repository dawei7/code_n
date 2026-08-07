from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        answer = None
        for index, value in enumerate(nums):
            if value != index:
                answer = value if answer is None else answer & value
        return 0 if answer is None else answer
