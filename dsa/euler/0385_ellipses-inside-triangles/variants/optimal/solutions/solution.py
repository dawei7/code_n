"""Project Euler Problem 385: Ellipses Inside Triangles.

Find A(10^9), the sum of the areas of all integer-coordinate triangles in [-n, n]^2 whose Steiner
inellipse has foci at (+/- sqrt(13), 0).
"""

from math import gcd
from typing import Dict, List, Set, Tuple

# Pell equation seeds for s^2 - 3*t^2 = K
_PELL_SEEDS: Dict[int, List[Tuple[int, int]]] = {
    468: [(24, 6), (30, 12)],
    117: [(12, 3), (15, 6)],
    36: [(6, 0)],
    9: [(3, 0)],
}


def _pell_step(s_val: int, t_val: int) -> Tuple[int, int]:
    """Advance (s, t) along the Pell branch using fundamental unit 2 + sqrt(3)."""
    return 2 * s_val + 3 * t_val, s_val + 2 * t_val


def _all_directions() -> List[Tuple[int, int, int, int]]:
    """Enumerate primitive pairs (m, n) with D = n^2 + 3*m^2 dividing 468."""
    dirs: List[Tuple[int, int, int, int]] = []
    for m in range(-12, 13):
        for n in range(-21, 22):
            if m == 0 and n == 0:
                continue
            if gcd(abs(m), abs(n)) != 1:
                continue
            d_val = n * n + 3 * m * m
            if d_val == 0 or 468 % d_val != 0:
                continue
            k_val = 468 // d_val
            if k_val in _PELL_SEEDS:
                dirs.append((m, n, d_val, k_val))
    return dirs


def solve(limit: int = 10**9) -> int:
    """Compute A(limit) using Pell orbit generation over primitive directional forms."""
    dirs = _all_directions()
    seen: Set[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]] = set()
    total_num_over_4 = 0

    for m, n, d_val, k_val in dirs:
        for s0, t0 in _PELL_SEEDS[k_val]:
            s, t = s0, t0
            while max(s, t) <= 6 * limit + 10:
                if s != 0 and t != 0:
                    for ss in (s, -s):
                        for tt in (t, -t):
                            if (ss * n) % 3 != 0:
                                continue
                            a = ss * m
                            b = -tt * n
                            c = (ss * n) // 3
                            d = tt * m

                            if ((a + c) & 1) or ((b + d) & 1):
                                continue

                            x1 = (a + c) // 2
                            y1 = (b + d) // 2
                            x2 = (c - a) // 2
                            y2 = (d - b) // 2
                            x3 = -c
                            y3 = -d

                            if (
                                max(
                                    abs(x1),
                                    abs(y1),
                                    abs(x2),
                                    abs(y2),
                                    abs(x3),
                                    abs(y3),
                                )
                                > limit
                            ):
                                continue

                            tri = tuple(
                                sorted(((x1, y1), (x2, y2), (x3, y3)))
                            )
                            if tri in seen:
                                continue
                            seen.add(tri)
                            total_num_over_4 += d_val * abs(s * t)

                s, t = _pell_step(s, t)

    return total_num_over_4 // 4


if __name__ == "__main__":
    print(solve())
