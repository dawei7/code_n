from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_index = {0: -1}
        balance = 0
        longest = 0
        for index, value in enumerate(nums):
            balance += 1 if value == 1 else -1
            if balance in first_index:
                longest = max(longest, index - first_index[balance])
            else:
                first_index[balance] = index
        return longest
