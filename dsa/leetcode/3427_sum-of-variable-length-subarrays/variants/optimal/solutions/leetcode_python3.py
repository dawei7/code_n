from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)

        total = 0
        for i, value in enumerate(nums):
            start = max(0, i - value)
            total += prefix[i + 1] - prefix[start]
        return total
