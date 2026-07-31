from collections import defaultdict
from typing import List


MODULO = 1_000_000_007


class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        totals = defaultdict(int)
        answer = 0

        for value in nums:
            added_count = (
                1 + counts[value - 1] + counts[value + 1]
            ) % MODULO
            added_total = (
                totals[value - 1]
                + totals[value + 1]
                + value * added_count
            ) % MODULO

            counts[value] = (counts[value] + added_count) % MODULO
            totals[value] = (totals[value] + added_total) % MODULO
            answer = (answer + added_total) % MODULO

        return answer
