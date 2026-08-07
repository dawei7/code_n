from math import atan2, pi
from typing import List


class Solution:
    def visiblePoints(
        self,
        points: List[List[int]],
        angle: int,
        location: List[int],
    ) -> int:
        origin_x, origin_y = location
        directions = []
        coincident = 0

        for point_x, point_y in points:
            delta_x = point_x - origin_x
            delta_y = point_y - origin_y
            if delta_x == 0 and delta_y == 0:
                coincident += 1
            else:
                directions.append(atan2(delta_y, delta_x))

        directions.sort()
        original_count = len(directions)
        directions.extend(value + 2 * pi for value in directions[:original_count])
        width = angle * pi / 180

        best = 0
        left = 0
        for right, direction in enumerate(directions):
            while direction - directions[left] > width + 1e-12:
                left += 1
            best = max(best, right - left + 1)

        return coincident + min(best, original_count)
