from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequencies = {}
        pairs = 0
        for value in nums:
            pairs += frequencies.get(value, 0)
            frequencies[value] = frequencies.get(value, 0) + 1
        return pairs
