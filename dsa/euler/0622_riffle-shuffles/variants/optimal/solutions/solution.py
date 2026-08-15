"""Project Euler Problem 622: Riffle Shuffles.

Find the sum of all values of n such that s(n) = 60, where s(n) is the minimum
number of riffle shuffles needed to restore a deck of size n.
"""

from typing import Dict, List


def _factorize(n: int) -> Dict[int, int]:
    factors: Dict[int, int] = {}
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            e = 0
            while temp % d == 0:
                temp //= d
                e += 1
            factors[d] = e
        d += 1
    if temp > 1:
        factors[temp] = 1
    return factors


def solve(target_k: int = 60) -> int:
    """Compute the sum of deck sizes n with s(n) = target_k by factoring 2^target_k - 1."""
    num = (1 << target_k) - 1
    factors = _factorize(num)

    divs = [1]
    for p, e in factors.items():
        new_divs = []
        p_pow = 1
        for _ in range(e + 1):
            for d in divs:
                new_divs.append(d * p_pow)
            p_pow *= p
        divs = new_divs

    # Find prime factors of target_k to determine maximal proper divisors
    k_factors = _factorize(target_k)
    max_divs = [target_k // p for p in k_factors]
    bad_nums = [(1 << d) - 1 for d in max_divs]

    valid_sum = 0
    for m in divs:
        if any(bad % m == 0 for bad in bad_nums):
            continue
        n = m + 1
        valid_sum += n

    return valid_sum


if __name__ == "__main__":
    print(solve())
