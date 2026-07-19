from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = [0] * 102
        for value in nums:
            counts[value + 1] += 1
        for index in range(1, len(counts)):
            counts[index] += counts[index - 1]
        return [counts[value] for value in nums]
