from math import hypot
from random import Random
from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:
        points = [(float(x), float(y)) for x, y in trees]
        Random(0).shuffle(points)
        epsilon = 1e-10

        def contains(circle: tuple[float, float, float], point: tuple[float, float]) -> bool:
            return hypot(point[0] - circle[0], point[1] - circle[1]) <= circle[2] + epsilon

        def diameter(
            first: tuple[float, float],
            second: tuple[float, float],
        ) -> tuple[float, float, float]:
            center_x = (first[0] + second[0]) / 2.0
            center_y = (first[1] + second[1]) / 2.0
            return center_x, center_y, hypot(first[0] - second[0], first[1] - second[1]) / 2.0

        def through_three(
            first: tuple[float, float],
            second: tuple[float, float],
            third: tuple[float, float],
        ) -> tuple[float, float, float]:
            ax, ay = first
            bx, by = second
            cx, cy = third
            divisor = 2.0 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))

            if abs(divisor) <= epsilon:
                candidates = [
                    diameter(first, second),
                    diameter(first, third),
                    diameter(second, third),
                ]
                return min(
                    (circle for circle in candidates if all(contains(circle, point) for point in (first, second, third))),
                    key=lambda circle: circle[2],
                )

            first_norm = ax * ax + ay * ay
            second_norm = bx * bx + by * by
            third_norm = cx * cx + cy * cy
            center_x = (
                first_norm * (by - cy)
                + second_norm * (cy - ay)
                + third_norm * (ay - by)
            ) / divisor
            center_y = (
                first_norm * (cx - bx)
                + second_norm * (ax - cx)
                + third_norm * (bx - ax)
            ) / divisor
            return center_x, center_y, hypot(center_x - ax, center_y - ay)

        circle = (points[0][0], points[0][1], 0.0)
        for first_index, first in enumerate(points):
            if contains(circle, first):
                continue
            circle = (first[0], first[1], 0.0)
            for second_index in range(first_index):
                second = points[second_index]
                if contains(circle, second):
                    continue
                circle = diameter(first, second)
                for third_index in range(second_index):
                    third = points[third_index]
                    if not contains(circle, third):
                        circle = through_three(first, second, third)

        return [circle[0], circle[1], circle[2]]
