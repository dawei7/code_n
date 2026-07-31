from bisect import bisect_right
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        tails: List[int] = []

        for value in nums:
            transformed = -value
            position = bisect_right(tails, transformed)
            if position == len(tails):
                tails.append(transformed)
            else:
                tails[position] = transformed

        return len(tails)
