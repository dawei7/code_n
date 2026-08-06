from collections import defaultdict
from math import gcd


def solve(points: list[list[int]]) -> int:
    n = len(points)
    if n <= 2:
        return n

    answer = 2
    for i, (x1, y1) in enumerate(points):
        directions: dict[tuple[int, int], int] = defaultdict(int)
        for j in range(i + 1, n):
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1
            if dx == 0:
                direction = (0, 1)
            elif dy == 0:
                direction = (1, 0)
            else:
                divisor = gcd(abs(dx), abs(dy))
                dx //= divisor
                dy //= divisor
                if dx < 0:
                    dx = -dx
                    dy = -dy
                direction = (dx, dy)
            directions[direction] += 1
        answer = max(answer, max(directions.values(), default=0) + 1)
    return answer
