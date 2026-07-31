from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rounds = 0
        for frequency in Counter(tasks).values():
            if frequency == 1:
                return -1
            rounds += (frequency + 2) // 3
        return rounds
