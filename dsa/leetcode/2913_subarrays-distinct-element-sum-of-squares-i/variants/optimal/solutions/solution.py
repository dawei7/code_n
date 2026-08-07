from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0

        for left in range(len(nums)):
            distinct = set()
            for right in range(left, len(nums)):
                distinct.add(nums[right])
                count = len(distinct)
                total += count * count

        return total
