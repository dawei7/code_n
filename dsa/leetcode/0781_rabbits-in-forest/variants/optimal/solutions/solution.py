from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        for answer, frequency in Counter(answers).items():
            group_size = answer + 1
            groups = (frequency + group_size - 1) // group_size
            total += groups * group_size
        return total
