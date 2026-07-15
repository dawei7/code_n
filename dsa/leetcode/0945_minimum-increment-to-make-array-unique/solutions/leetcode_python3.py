from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        limit = max(nums) + len(nums)
        frequency = [0] * (limit + 1)
        for value in nums:
            frequency[value] += 1

        moves = 0
        for value in range(limit):
            excess = frequency[value] - 1
            if excess > 0:
                frequency[value + 1] += excess
                moves += excess

        return moves
