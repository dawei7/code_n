from math import sqrt
from typing import List


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        coordinates = {tuple(point) for point in points}
        minimum = float("inf")

        for ax, ay in coordinates:
            for bx, by in coordinates:
                if (ax, ay) == (bx, by):
                    continue
                abx, aby = bx - ax, by - ay
                for cx, cy in coordinates:
                    if (ax, ay) == (cx, cy) or (bx, by) == (cx, cy):
                        continue
                    acx, acy = cx - ax, cy - ay
                    if abx * acx + aby * acy != 0:
                        continue
                    if (bx + cx - ax, by + cy - ay) not in coordinates:
                        continue
                    area = sqrt((abx * abx + aby * aby) * (acx * acx + acy * acy))
                    minimum = min(minimum, area)

        return 0.0 if minimum == float("inf") else minimum
