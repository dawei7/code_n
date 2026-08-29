"""Project Euler Problem 461: Almost Pi.

Find g(10000) = a^2 + b^2 + c^2 + d^2 for non-negative integers a, b, c, d
minimizing |f_n(a) + f_n(b) + f_n(c) + f_n(d) - pi|, where f_n(k) = e^(k/n) - 1.
"""

from math import exp, isqrt, log, pi
from typing import List, Tuple


def solve(n: int = 10000) -> int:
    """Compute g(n) using meet-in-the-middle 2-sum generation and two-pointer search."""
    target = pi
    kmax = int(n * log(target + 1.0)) + 2
    f_vals = [exp(k / n) - 1.0 for k in range(kmax + 1)]

    vals: List[float] = []
    pairs: List[int] = []

    for a in range(kmax + 1):
        fa = f_vals[a]
        if fa > target:
            break
        for b in range(a, kmax + 1):
            fab = fa + f_vals[b]
            if fab > target:
                break
            vals.append(fab)
            pairs.append((a << 16) | b)

    order = sorted(range(len(vals)), key=lambda i: vals[i])

    best_err = float("inf")
    best_tuple: Tuple[int, int, int, int] = (0, 0, 0, 0)

    l_idx = 0
    r_idx = len(order) - 1

    while l_idx <= r_idx:
        idx_l = order[l_idx]
        idx_r = order[r_idx]
        tot = vals[idx_l] + vals[idx_r]
        err = abs(tot - target)
        if err < best_err:
            best_err = err
            packed_l = pairs[idx_l]
            packed_r = pairs[idx_r]
            best_tuple = (
                packed_l >> 16,
                packed_l & 0xFFFF,
                packed_r >> 16,
                packed_r & 0xFFFF,
            )

        if tot < target:
            l_idx += 1
        else:
            r_idx -= 1

    a, b, c, d = best_tuple
    return a * a + b * b + c * c + d * d


if __name__ == "__main__":
    print(solve())
