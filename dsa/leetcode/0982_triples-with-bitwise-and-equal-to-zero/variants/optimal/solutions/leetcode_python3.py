from collections import Counter
from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        value_counts = Counter(nums)
        pair_counts = Counter(
            first & second
            for first in nums
            for second in nums
        )

        answer = 0
        for value, occurrences in value_counts.items():
            compatible_pairs = sum(
                count
                for mask, count in pair_counts.items()
                if mask & value == 0
            )
            answer += occurrences * compatible_pairs
        return answer
