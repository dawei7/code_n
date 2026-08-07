from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = Counter(map(tuple, grid))
        return sum(row_counts[column] for column in zip(*grid))
