"""Optimal solution for LeetCode 1001: Grid Illumination."""

from collections import Counter


def solve(n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
    active = set()
    rows: Counter[int] = Counter()
    cols: Counter[int] = Counter()
    diag: Counter[int] = Counter()
    anti: Counter[int] = Counter()

    for r, c in lamps:
        if (r, c) in active:
            continue
        active.add((r, c))
        rows[r] += 1
        cols[c] += 1
        diag[r - c] += 1
        anti[r + c] += 1

    answer: list[int] = []
    for r, c in queries:
        answer.append(1 if rows[r] or cols[c] or diag[r - c] or anti[r + c] else 0)
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < n) or (nr, nc) not in active:
                    continue
                active.remove((nr, nc))
                rows[nr] -= 1
                cols[nc] -= 1
                diag[nr - nc] -= 1
                anti[nr + nc] -= 1
    return answer
