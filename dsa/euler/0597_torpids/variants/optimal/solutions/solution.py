"""Project Euler Problem 597: Torpids.

Find p(13, 1800) rounded to 10 decimal places, where p(n, L) is the probability
that the finishing order of n boats on an L-metre course is an even permutation.
"""

from fractions import Fraction
from functools import lru_cache


def _round_fraction(x: Fraction, digits: int) -> str:
    num, den = x.numerator, x.denominator
    scale = 10 ** (digits + 1)
    q, _ = divmod(num * scale, den)
    last = q % 10
    q //= 10
    if last >= 5:
        q += 1
    int_part = q // (10**digits)
    frac_part = q % (10**digits)
    if digits == 0:
        return str(int_part)
    return f"{int_part}.{frac_part:0{digits}d}"


def _probability_even(n: int, l_dist: int, spacing: int = 40) -> Fraction:
    alpha = Fraction(l_dist, spacing)
    t0 = alpha + 1

    @lru_cache(maxsize=None)
    def expected_sign(l_idx: int, r_idx: int, t_coord: Fraction) -> Fraction:
        if l_idx >= r_idx:
            return Fraction(1, 1)

        count = r_idx - l_idx + 1
        sum_j = (l_idx + r_idx) * count // 2
        s_val = Fraction(count, 1) * t_coord - sum_j

        total = Fraction(0, 1)
        for m in range(l_idx, r_idx + 1):
            pm = (t_coord - m) / s_val
            sign_flip = -1 if ((m - l_idx) & 1) else 1
            left = expected_sign(l_idx, m - 1, Fraction(m, 1))
            right = expected_sign(m + 1, r_idx, t_coord)
            total += pm * sign_flip * left * right
        return total

    e_sign = expected_sign(1, n, t0)
    return (Fraction(1, 1) + e_sign) / 2


def solve(n: int = 13, l_dist: int = 1800) -> str:
    """Compute p(n, l_dist) using exponential race decomposition and parity sign recurrence."""
    prob = _probability_even(n, l_dist)
    digits = 10
    num, den = prob.numerator, prob.denominator
    scale = 1
    for _ in range(digits + 1):
        scale *= 10
    q, _ = divmod(num * scale, den)
    last = q % 10
    q //= 10
    if last >= 5:
        q += 1
    int_part = q // (10**digits)
    frac_part = q % (10**digits)
    return f"{int_part}.{frac_part:0{digits}d}"


if __name__ == "__main__":
    print(solve())
