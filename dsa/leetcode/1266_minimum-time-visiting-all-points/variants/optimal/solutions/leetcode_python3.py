from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            total += max(abs(x2 - x1), abs(y2 - y1))
        return total
