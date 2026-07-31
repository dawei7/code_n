from collections import Counter
from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        frequencies = Counter(nums)
        return sum(
            value * frequency
            for value, frequency in frequencies.items()
            if frequency % k == 0
        )
