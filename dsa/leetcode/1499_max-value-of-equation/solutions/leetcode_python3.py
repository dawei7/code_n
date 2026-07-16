from collections import deque
from typing import List


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        candidates = deque()
        best = -10**30

        for x, y in points:
            while candidates and x - candidates[0][0] > k:
                candidates.popleft()

            if candidates:
                best = max(best, x + y + candidates[0][1])

            score = y - x
            while candidates and candidates[-1][1] <= score:
                candidates.pop()
            candidates.append((x, score))

        return best
