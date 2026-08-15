"""Project Euler Problem 454: Diophantine Reciprocals III.

Find F(10^12), where F(L) is the number of solutions to 1/x + 1/y = 1/n
satisfying x < y <= L in positive integers.
"""

from array import array
from math import isqrt
from typing import List


def _build_spf(limit: int) -> array:
    spf = array("i", [0]) * (limit + 1)
    primes: List[int] = []
    if limit >= 1:
        spf[1] = 1
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            v = i * p
            if v > limit:
                break
            spf[v] = p
            if p == spf[i]:
                break
    return spf


def _sum_floor_segment(x: int, lo: int, hi: int) -> int:
    if hi <= lo or x <= 0:
        return 0
    res = 0
    i = lo + 1
    while i <= hi:
        q = x // i
        if q == 0:
            break
        j = x // q
        if j > hi:
            j = hi
        res += q * (j - i + 1)
        i = j + 1
    return res


def solve(limit: int = 10**12) -> int:
    """Compute F(limit) using coprime parametrization, Möbius inversion, and quotient grouping."""
    b_limit = isqrt(limit)
    spf = _build_spf(b_limit)

    total = 0
    sum_floor = _sum_floor_segment

    for n in range(2, b_limit + 1):
        tmp = n
        primes: List[int] = []
        last = 0
        while tmp > 1:
            p = spf[tmp]
            tmp //= p
            if p != last:
                primes.append(p)
                last = p

        divs = [1]
        mus = [1]
        for p in primes:
            m = len(divs)
            for i in range(m):
                divs.append(divs[i] * p)
                mus.append(-mus[i])

        ln = limit // n

        for idx in range(len(divs)):
            d = divs[idx]
            mu = mus[idx]

            k = n // d
            if k <= 1:
                continue

            x = ln // d
            if x == 0:
                continue

            total += mu * sum_floor(x, k, 2 * k - 1)

    return total


if __name__ == "__main__":
    print(solve())
