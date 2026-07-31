import math


def solve(sides: list[int]) -> list[float]:
    a, b, c = sorted(sides)
    if a + b <= c:
        return []

    angles: list[float] = []
    for opposite, adjacent_1, adjacent_2 in (
        (a, b, c),
        (b, a, c),
        (c, a, b),
    ):
        numerator = (
            adjacent_1 * adjacent_1
            + adjacent_2 * adjacent_2
            - opposite * opposite
        )
        cosine = numerator / (2 * adjacent_1 * adjacent_2)
        cosine = max(-1.0, min(1.0, cosine))
        angles.append(math.degrees(math.acos(cosine)))

    return angles
