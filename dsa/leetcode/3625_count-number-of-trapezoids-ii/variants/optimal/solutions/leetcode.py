from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        segments_by_slope = defaultdict(int)
        segments_by_line = defaultdict(int)
        diagonals_by_midpoint = defaultdict(int)
        diagonals_by_midpoint_and_slope = defaultdict(int)

        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i + 1 :]:
                dx = x2 - x1
                dy = y2 - y1
                divisor = gcd(abs(dx), abs(dy))
                dx //= divisor
                dy //= divisor
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                slope = (dy, dx)
                line = (slope, dy * x1 - dx * y1)
                midpoint = (x1 + x2, y1 + y2)

                segments_by_slope[slope] += 1
                segments_by_line[line] += 1
                diagonals_by_midpoint[midpoint] += 1
                diagonals_by_midpoint_and_slope[(midpoint, slope)] += 1

        parallel_side_pairs = sum(count * (count - 1) // 2 for count in segments_by_slope.values()) - sum(
            count * (count - 1) // 2 for count in segments_by_line.values()
        )

        parallelograms = sum(count * (count - 1) // 2 for count in diagonals_by_midpoint.values()) - sum(
            count * (count - 1) // 2 for count in diagonals_by_midpoint_and_slope.values()
        )

        return parallel_side_pairs - parallelograms
