"""Project Euler Problem 770: Delphi Flip.

Find g(1.9999), the smallest n so that A can guarantee at least 1.9999 grams of gold
in the Delphi Flip game with n TAKEs and n GIVEs.
"""

import math
from typing import Tuple


def _ln_p_central_binom_over_4n(n: int) -> float:
    nf = float(n)
    inv = 1.0 / nf
    inv2 = inv * inv
    inv3 = inv2 * inv
    inv5 = inv3 * inv2
    return (
        -0.5 * math.log(math.pi * nf)
        - 0.125 * inv
        + (1.0 / 192.0) * inv3
        - (1.0 / 640.0) * inv5
    )


def _p_leq_r_exact(n: int, r_num: int, r_den: int) -> bool:
    c = math.comb(2 * n, n)
    return c * r_den <= (1 << (2 * n)) * r_num


def solve(x_num: int = 19999, x_den: int = 10000) -> int:
    """Compute g(x_num / x_den) using minimax central binomial closed form and Stirling series."""
    r_num = 2 * x_den - x_num
    r_den = x_num
    g = math.gcd(r_num, r_den)
    r_num //= g
    r_den //= g

    r = r_num / r_den
    if r == 0.0:
        return 0

    n_est = int(1.0 / (math.pi * r * r))
    if n_est < 20000:
        n = 0
        while not _p_leq_r_exact(n, r_num, r_den):
            n += 1
        return n

    ln_r = math.log(r_num) - math.log(r_den)
    n = max(1, n_est - 10)
    while _ln_p_central_binom_over_4n(n) > ln_r:
        n += 1
    while n > 1 and _ln_p_central_binom_over_4n(n - 1) <= ln_r:
        n -= 1
    return n


if __name__ == "__main__":
    print(solve())
