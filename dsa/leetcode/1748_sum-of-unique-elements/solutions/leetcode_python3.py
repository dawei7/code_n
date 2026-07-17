from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        frequency = [0] * 101
        for value in nums:
            frequency[value] += 1

        return sum(value for value in range(1, 101) if frequency[value] == 1)
