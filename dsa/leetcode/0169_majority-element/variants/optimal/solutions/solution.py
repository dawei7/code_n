from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        balance = 0
        for value in nums:
            if balance == 0:
                candidate = value
            balance += 1 if value == candidate else -1
        return candidate
