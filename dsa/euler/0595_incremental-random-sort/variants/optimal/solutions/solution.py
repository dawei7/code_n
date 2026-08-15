"""Project Euler Problem 595: Incremental Random Sort.

Find S(52) rounded to 8 decimal places, where S(n) is the expected number of shuffles
to sort a random permutation of n cards with incremental contiguous-run gluing.
"""

from decimal import Decimal, ROUND_HALF_UP, getcontext
from fractions import Fraction
from typing import List


def _build_factorials(n: int) -> List[int]:
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i
    return fact


def _comb(n: int, k: int, fact: List[int]) -> int:
    if k < 0 or k > n:
        return 0
    if k > n - k:
        k = n - k
    return fact[n] // (fact[k] * fact[n - k])


def _succession_counts_upto(n: int, fact: List[int]) -> List[List[int]]:
    a: List[List[int]] = [[] for _ in range(n + 1)]
    a[1] = [1]
    for m in range(2, n + 1):
        row = [0] * m
        for r in range(0, m):
            c1 = _comb(m - 1, r, fact)
            s = 0
            for j in range(0, m - r):
                k = m - r - j
                term = _comb(m - 1 - r, j, fact) * fact[k]
                if j & 1:
                    s -= term
                else:
                    s += term
            row[r] = c1 * s
        a[m] = row
    return a


def solve(n: int = 52) -> str:
    """Compute S(n) as an exact fraction and format rounded to 8 decimal places."""
    fact = _build_factorials(n)
    a = _succession_counts_upto(n, fact)

    t_arr = [Fraction(0, 1)] * (n + 1)
    t_arr[1] = Fraction(0, 1)

    for m in range(2, n + 1):
        denom = fact[m] - a[m][0]
        num = Fraction(fact[m], 1)
        for r in range(1, m):
            num += Fraction(a[m][r], 1) * t_arr[m - r]
        t_arr[m] = num / denom

    sn = Fraction(0, 1)
    for r in range(0, n):
        sn += Fraction(a[n][r], fact[n]) * t_arr[n - r]

    getcontext().prec = 80
    d = Decimal(sn.numerator) / Decimal(sn.denominator)
    ans = d.quantize(Decimal("0.00000001"), rounding=ROUND_HALF_UP)
    return format(ans, "f")


if __name__ == "__main__":
    print(solve())
