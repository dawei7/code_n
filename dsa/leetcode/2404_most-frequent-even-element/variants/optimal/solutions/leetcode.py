from collections import Counter
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = Counter(value for value in nums if value % 2 == 0)
        if not counts:
            return -1
        return min(counts, key=lambda value: (-counts[value], value))
