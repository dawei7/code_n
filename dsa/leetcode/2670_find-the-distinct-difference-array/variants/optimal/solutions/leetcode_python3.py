from typing import List
from collections import Counter


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        suffix_counts = Counter(nums)
        prefix_values = set()
        differences = []

        for value in nums:
            prefix_values.add(value)
            suffix_counts[value] -= 1
            if suffix_counts[value] == 0:
                del suffix_counts[value]
            differences.append(len(prefix_values) - len(suffix_counts))

        return differences
