"""Project Euler Problem 736: Paths to Equality.

Find the final value of the unique path to equality for (45, 90) with smallest odd length.
"""

from itertools import combinations_with_replacement
from typing import List, Sequence, Tuple

Point = Tuple[int, int]


def _apply_ops(start: Point, ops: Sequence[str]) -> List[Point]:
    x, y = start
    states: List[Point] = [(x, y)]
    for op in ops:
        if op == "r":
            x, y = x + 1, y * 2
        elif op == "s":
            x, y = x * 2, y + 1
        states.append((x, y))
    return states


def _rhs_from_positions(t: int, positions: Sequence[int]) -> int:
    s = len(positions)
    idx = 0
    total = 0
    for j in range(t):
        while idx < s and positions[idx] <= j:
            idx += 1
        total += 1 << idx
    return total


def solve(a: int = 45, b: int = 90) -> int:
    """Find the final value of the unique path to equality for (a, b) with smallest odd length."""
    start = (a, b)

    for t in range(a, 200):
        s = t - a
        if s < 0:
            continue

        sols: List[Tuple[int, ...]] = []
        for pos in combinations_with_replacement(range(t), s):
            lhs = sum(1 << p for p in pos)
            rhs = _rhs_from_positions(t, pos)
            if lhs == rhs:
                sols.append(pos)

        if not sols:
            continue

        pos = sols[0]
        c = [0] * (t + 1)
        for p in pos:
            c[p] += 1
        c[t] = a

        ops_rev: List[str] = []
        for j in range(t):
            ops_rev.extend(["R"] * c[j])
            ops_rev.append("S")
        ops_rev.extend(["R"] * c[t])

        inv = {"R": "r", "S": "s"}
        ops_fwd = [inv[o] for o in reversed(ops_rev)]

        states = _apply_ops(start, ops_fwd)
        final_value = states[-1][0]
        return final_value

    raise RuntimeError("No solution found in the searched range.")


if __name__ == "__main__":
    print(solve())
