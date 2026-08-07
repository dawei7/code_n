from collections import Counter
from typing import List


class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        frequencies = list(Counter(balls).values())

        for smaller_size in range(min(frequencies), 0, -1):
            total_groups = 0
            for frequency in frequencies:
                groups = (frequency + smaller_size) // (smaller_size + 1)
                if groups * smaller_size > frequency:
                    break
                total_groups += groups
            else:
                return total_groups

        return len(balls)
