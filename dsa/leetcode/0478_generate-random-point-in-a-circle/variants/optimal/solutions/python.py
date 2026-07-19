"""Deterministic uniform-area point trace for LeetCode 478."""

from math import cos, pi, sin, sqrt


def solve(
    radius: float,
    x_center: float,
    y_center: float,
    random_values: list[float],
    draws: int,
) -> list[list[float]]:
    position = 0

    def uniform() -> float:
        nonlocal position
        value = random_values[position % len(random_values)]
        position += 1
        return value

    points = []
    for _ in range(draws):
        distance = radius * sqrt(uniform())
        angle = 2 * pi * uniform()
        points.append(
            [x_center + distance * cos(angle), y_center + distance * sin(angle)]
        )
    return points
