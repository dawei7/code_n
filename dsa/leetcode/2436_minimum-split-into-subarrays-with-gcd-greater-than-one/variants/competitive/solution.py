from math import gcd
from typing import List


class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        groups = 1
        common = 0

        for value in nums:
            extended = gcd(common, value)
            if extended == 1:
                groups += 1
                common = value
            else:
                common = extended

        return groups
