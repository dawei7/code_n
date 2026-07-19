from math import hypot
from random import Random


def solve(trees: list[list[int]]) -> list[float]:
    points = [(float(x), float(y)) for x, y in trees]
    Random(0).shuffle(points)
    epsilon = 1e-10

    def contains(circle: tuple[float, float, float], point: tuple[float, float]) -> bool:
        return hypot(point[0] - circle[0], point[1] - circle[1]) <= circle[2] + epsilon

    def diameter(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float, float]:
        x = (a[0] + b[0]) / 2.0
        y = (a[1] + b[1]) / 2.0
        return x, y, hypot(a[0] - b[0], a[1] - b[1]) / 2.0

    def through_three(a: tuple[float, float], b: tuple[float, float], c: tuple[float, float]) -> tuple[float, float, float]:
        ax, ay = a
        bx, by = b
        cx, cy = c
        divisor = 2.0 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        if abs(divisor) <= epsilon:
            candidates = (diameter(a, b), diameter(a, c), diameter(b, c))
            return min(
                (circle for circle in candidates if all(contains(circle, point) for point in (a, b, c))),
                key=lambda circle: circle[2],
            )
        a_norm = ax * ax + ay * ay
        b_norm = bx * bx + by * by
        c_norm = cx * cx + cy * cy
        x = (a_norm * (by - cy) + b_norm * (cy - ay) + c_norm * (ay - by)) / divisor
        y = (a_norm * (cx - bx) + b_norm * (ax - cx) + c_norm * (bx - ax)) / divisor
        return x, y, hypot(x - ax, y - ay)

    circle = (points[0][0], points[0][1], 0.0)
    for i, first in enumerate(points):
        if contains(circle, first):
            continue
        circle = (first[0], first[1], 0.0)
        for j in range(i):
            second = points[j]
            if contains(circle, second):
                continue
            circle = diameter(first, second)
            for k in range(j):
                third = points[k]
                if not contains(circle, third):
                    circle = through_three(first, second, third)
    return [circle[0], circle[1], circle[2]]
