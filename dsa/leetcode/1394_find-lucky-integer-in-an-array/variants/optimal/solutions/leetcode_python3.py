from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequencies = Counter(arr)
        return max(
            (value for value, frequency in frequencies.items() if value == frequency),
            default=-1,
        )
