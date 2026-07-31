import math


def solve(sides: list[int]) -> list[float]:
    a, b, c = sorted(sides)
    if a + b <= c:
        return []

    def angle(opposite: int, adjacent_1: int, adjacent_2: int) -> float:
        cosine = (adjacent_1 * adjacent_1 + adjacent_2 * adjacent_2 - opposite * opposite) / (
            2 * adjacent_1 * adjacent_2
        )
        return math.degrees(math.acos(max(-1.0, min(1.0, cosine))))

    return [angle(a, b, c), angle(b, a, c), angle(c, a, b)]
