from collections import Counter
from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        frequencies = Counter(nums)
        return [
            value
            for value, count in frequencies.items()
            if count == 1
            and value - 1 not in frequencies
            and value + 1 not in frequencies
        ]
