from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        difference = abs(goal - sum(nums))
        return (difference + limit - 1) // limit
