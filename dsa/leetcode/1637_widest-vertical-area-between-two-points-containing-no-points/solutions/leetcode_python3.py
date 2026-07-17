from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coordinates = sorted(point[0] for point in points)
        return max(
            right - left
            for left, right in zip(x_coordinates, x_coordinates[1:])
        )
