"""Deterministic weighted lattice-point draws for LeetCode 497."""

from bisect import bisect_right


def solve(
    rects: list[list[int]],
    random_values: list[float],
    draws: int,
) -> list[list[int]]:
    prefix: list[int] = []
    total = 0
    for x1, y1, x2, y2 in rects:
        total += (x2 - x1 + 1) * (y2 - y1 + 1)
        prefix.append(total)

    points: list[list[int]] = []
    for draw in range(draws):
        uniform = random_values[draw % len(random_values)]
        ticket = min(int(uniform * total), total - 1)
        rectangle_index = bisect_right(prefix, ticket)
        previous_total = prefix[rectangle_index - 1] if rectangle_index else 0
        offset = ticket - previous_total
        x1, y1, x2, _ = rects[rectangle_index]
        width = x2 - x1 + 1
        points.append([x1 + offset % width, y1 + offset // width])
    return points
