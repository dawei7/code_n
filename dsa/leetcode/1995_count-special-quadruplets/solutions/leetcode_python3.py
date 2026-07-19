from collections import Counter
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        differences = Counter()
        total = 0

        for second in range(len(nums) - 3, 0, -1):
            third = second + 1
            for fourth in range(third + 1, len(nums)):
                differences[nums[fourth] - nums[third]] += 1

            for first in range(second):
                total += differences[nums[first] + nums[second]]

        return total
