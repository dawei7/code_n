"""Project Euler Problem 499: St. Petersburg Lottery.

Find p_15(10^9), the probability that a gambler with initial fortune 10^9
never runs out of money playing the St. Petersburg lottery with cost m = 15 per game,
rounded to 7 decimal places in the form 0.abcdefg.
"""

from math import expm1


def _f_expm1(t: float, m: int) -> float:
    s = 0.0
    c = 0.0
    pow2 = 1.0
    weight = 0.5

    for _ in range(200):
        term = weight * expm1(pow2 * t)
        y = term - c
        tmp = s + y
        c = (tmp - s) - y
        s = tmp

        if weight < 2.0**-90:
            break

        pow2 *= 2.0
        weight *= 0.5

    return expm1(m * t) - s


def solve(m: int = 15, s: int = 10**9) -> str:
    """Compute p_m(s) using martingale characteristic root equation and Cramer-Lundberg bisection."""
    hi = -1e-12
    f_hi = _f_expm1(hi, m)

    while f_hi <= 0.0:
        hi *= 0.5
        f_hi = _f_expm1(hi, m)

    lo = hi
    f_lo = f_hi
    while f_lo > 0.0:
        lo *= 2.0
        f_lo = _f_expm1(lo, m)
        if lo < -100.0:
            raise RuntimeError("Failed to bracket root.")

    for _ in range(120):
        mid = (lo + hi) * 0.5
        f_mid = _f_expm1(mid, m)
        if f_mid > 0.0:
            hi = mid
        else:
            lo = mid

    t = (lo + hi) * 0.5
    ans = -expm1(t * (s - m + 1)) if s >= m else 0.0
    return f"{ans:.7f}"


if __name__ == "__main__":
    print(solve())
