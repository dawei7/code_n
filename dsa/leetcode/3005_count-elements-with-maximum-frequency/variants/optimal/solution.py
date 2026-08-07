from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = Counter(nums)
        maximum = max(frequencies.values())
        return sum(count for count in frequencies.values() if count == maximum)
