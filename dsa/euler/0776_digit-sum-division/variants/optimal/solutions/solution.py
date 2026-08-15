"""Project Euler Problem 776: Digit Sum Division.

Find F(1234567890123456789) where F(N) = sum_{n=1}^N n / d(n),
formatted in scientific notation rounded to 12 digits after the decimal point.
"""

from decimal import Decimal, ROUND_HALF_UP, getcontext
from typing import List


def _sum_by_digit_sum_upto(n: int) -> List[int]:
    if n < 0:
        return []

    digits = list(map(int, str(n)))
    L = len(digits)
    max_sum = 9 * L

    cnt_tight = [0] * (max_sum + 1)
    sum_tight = [0] * (max_sum + 1)
    cnt_tight[0] = 1

    cnt_loose = [0] * (max_sum + 1)
    sum_loose = [0] * (max_sum + 1)

    for lim in digits:
        ncnt_tight = [0] * (max_sum + 1)
        nsum_tight = [0] * (max_sum + 1)
        ncnt_loose = [0] * (max_sum + 1)
        nsum_loose = [0] * (max_sum + 1)

        for s, c in enumerate(cnt_loose):
            if not c:
                continue
            v10 = sum_loose[s] * 10
            for d in range(10):
                ns = s + d
                ncnt_loose[ns] += c
                nsum_loose[ns] += v10 + c * d

        for s, c in enumerate(cnt_tight):
            if not c:
                continue
            v10 = sum_tight[s] * 10
            for d in range(lim + 1):
                ns = s + d
                if d == lim:
                    ncnt_tight[ns] += c
                    nsum_tight[ns] += v10 + c * d
                else:
                    ncnt_loose[ns] += c
                    nsum_loose[ns] += v10 + c * d

        cnt_tight, sum_tight = ncnt_tight, nsum_tight
        cnt_loose, sum_loose = ncnt_loose, nsum_loose

    return [sum_tight[s] + sum_loose[s] for s in range(max_sum + 1)]


def solve(N: int = 1234567890123456789, prec: int = 120) -> str:
    """Compute F(N) using exact digit DP and format in 12-decimal scientific notation."""
    getcontext().prec = prec
    getcontext().rounding = ROUND_HALF_UP

    sums = _sum_by_digit_sum_upto(N)
    total = Decimal(0)
    for s in range(1, len(sums)):
        if sums[s]:
            total += Decimal(sums[s]) / Decimal(s)

    formatted = format(total, ".12E")
    mant, exp = formatted.split("E")
    return f"{mant}e{int(exp)}"


if __name__ == "__main__":
    print(solve())
