from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        largest_doubled_area = 0
        for first in range(len(points) - 2):
            ax, ay = points[first]
            for second in range(first + 1, len(points) - 1):
                bx, by = points[second]
                for third in range(second + 1, len(points)):
                    cx, cy = points[third]
                    doubled_area = abs((bx - ax) * (cy - ay) - (by - ay) * (cx - ax))
                    largest_doubled_area = max(largest_doubled_area, doubled_area)
        return largest_doubled_area / 2.0
