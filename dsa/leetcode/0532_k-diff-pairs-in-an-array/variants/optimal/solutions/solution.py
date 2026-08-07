from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        frequencies = Counter(nums)
        if k == 0:
            return sum(frequency >= 2 for frequency in frequencies.values())
        return sum(value + k in frequencies for value in frequencies)
