"""Optimal app-local solution for LeetCode 1499."""

from collections import deque


def solve(points: list[list[int]], k: int) -> int:
    """Return the maximum equation value among horizontally close point pairs."""
    candidates: deque[tuple[int, int]] = deque()
    best = -10**30

    for x, y in points:
        while candidates and x - candidates[0][0] > k:
            candidates.popleft()

        if candidates:
            best = max(best, x + y + candidates[0][1])

        score = y - x
        while candidates and candidates[-1][1] <= score:
            candidates.pop()
        candidates.append((x, score))

    return best
