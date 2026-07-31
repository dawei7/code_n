from math import cos, pi, sin, sqrt


def solve(
    radius: float,
    x_center: float,
    y_center: float,
    random_values: list[float],
    draws: int,
) -> list[list[float]]:
    position = 0

    def random() -> float:
        nonlocal position
        value = random_values[position % len(random_values)]
        position += 1
        return value

    def randPoint() -> list[float]:
        distance = radius * sqrt(random())
        angle = 2 * pi * random()
        return [
            x_center + distance * cos(angle),
            y_center + distance * sin(angle),
        ]

    return [randPoint() for _ in range(draws)]
