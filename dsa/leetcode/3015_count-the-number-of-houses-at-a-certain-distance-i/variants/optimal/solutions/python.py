from typing import List


def solve(n: int, x: int, y: int) -> List[int]:
    counts = [0] * n
    for first in range(1, n + 1):
        for second in range(first + 1, n + 1):
            distance = min(
                second - first,
                abs(first - x) + 1 + abs(second - y),
                abs(first - y) + 1 + abs(second - x),
            )
            counts[distance - 1] += 2
    return counts
