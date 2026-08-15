"""Project Euler Problem 687: Shuffling Cards.

Find the probability that the number of perfect ranks (ranks with no two cards adjacent in a shuffled deck of 52 cards)
is prime, rounded to 10 decimal places.
"""

from decimal import Decimal, getcontext, ROUND_HALF_UP
from math import comb, factorial
from typing import List


def _poly_mul(a: List[int], b: List[int]) -> List[int]:
    res = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if bj == 0:
                continue
            res[i + j] += ai * bj
    return res


def solve(ranks: int = 13, copies: int = 4) -> str:
    """Compute the probability that the count of perfect ranks is prime via inclusion-exclusion polynomial powers."""
    n_cards = ranks * copies
    base = factorial(copies)

    q = [1, -12, 36, -24]

    fact = [1] * (n_cards + 1)
    for i in range(2, n_cards + 1):
        fact[i] = fact[i - 1] * i

    q_pow: List[List[int]] = [[1]]
    for _ in range(1, ranks + 1):
        q_pow.append(_poly_mul(q_pow[-1], q))

    denom = base**ranks
    n_fixed = [0] * (ranks + 1)
    for m in range(ranks + 1):
        coeff = q_pow[m]
        num = 0
        for b, c in enumerate(coeff):
            num += fact[n_cards - b] * c
        n_fixed[m] = num // denom

    total = n_fixed[0]

    z = [0] * (ranks + 1)
    for k in range(ranks + 1):
        s = 0
        for m in range(k, ranks + 1):
            s += ((-1) ** (m - k)) * comb(ranks - k, m - k) * n_fixed[m]
        z[k] = s

    x = [0] * (ranks + 1)
    for k in range(ranks + 1):
        x[k] = comb(ranks, k) * z[k]

    primes = {2, 3, 5, 7, 11, 13}
    good = sum(x[k] for k in primes if k <= ranks)

    getcontext().prec = 60
    ans = (Decimal(good) / Decimal(total)).quantize(
        Decimal("0.0000000000"), rounding=ROUND_HALF_UP
    )
    return format(ans, "f")


if __name__ == "__main__":
    print(solve())
