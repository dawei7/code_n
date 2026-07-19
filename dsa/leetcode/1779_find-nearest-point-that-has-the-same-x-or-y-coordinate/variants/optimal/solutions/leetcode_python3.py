from typing import List


class Solution:
    def nearestValidPoint(
        self,
        x: int,
        y: int,
        points: List[List[int]],
    ) -> int:
        best_index = -1
        best_distance = float("inf")
        for index, (point_x, point_y) in enumerate(points):
            if point_x == x or point_y == y:
                distance = abs(point_x - x) + abs(point_y - y)
                if distance < best_distance:
                    best_distance = distance
                    best_index = index
        return best_index
