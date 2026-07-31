from typing import List


class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        uncovered = []
        next_uncovered = 0

        for start, end in sorted(ranges):
            if next_uncovered < start:
                uncovered.append([next_uncovered, start - 1])
            next_uncovered = max(next_uncovered, end + 1)

        if next_uncovered < n:
            uncovered.append([next_uncovered, n - 1])
        return uncovered
