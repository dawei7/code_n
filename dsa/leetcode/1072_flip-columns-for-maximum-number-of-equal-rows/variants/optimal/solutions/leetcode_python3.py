from collections import Counter
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = Counter()
        for row in matrix:
            first = row[0]
            pattern = tuple(value ^ first for value in row)
            patterns[pattern] += 1
        return max(patterns.values())
