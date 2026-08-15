"""Project Euler Problem 516: 5-smooth Totients.

Find S(10^12) mod 2^32, where S(L) is the sum of all numbers n <= L
such that Euler's totient phi(n) is 5-smooth (a Hamming number).
"""

import bisect
from typing import List

MOD = 1 << 32


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        return True
    if any(
        n % p == 0 for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    ):
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def solve(limit: int = 10**12, mod: int = MOD) -> int:
    """Compute S(L) mod mod by generating 5-smooth numbers and squarefree special primes."""
    smooth: List[int] = []
    p2 = 1
    while p2 <= limit:
        p3 = 1
        while p2 * p3 <= limit:
            p5 = 1
            while p2 * p3 * p5 <= limit:
                smooth.append(p2 * p3 * p5)
                p5 *= 5
            p3 *= 3
        p2 *= 2
    smooth.sort()

    special_primes: List[int] = []
    for h in smooth:
        p = h + 1
        if p > 5 and p <= limit and _is_prime(p):
            special_primes.append(p)
    special_primes.sort()

    products: List[int] = []

    def dfs(idx: int, cur_prod: int) -> None:
        products.append(cur_prod)
        for i in range(idx, len(special_primes)):
            p_val = special_primes[i]
            if cur_prod * p_val > limit:
                break
            dfs(i + 1, cur_prod * p_val)

    dfs(0, 1)

    smooth_prefix: List[int] = [0] * (len(smooth) + 1)
    for i in range(len(smooth)):
        smooth_prefix[i + 1] = smooth_prefix[i] + smooth[i]

    total = 0
    for q in products:
        max_h = limit // q
        idx = bisect.bisect_right(smooth, max_h)
        sum_h = smooth_prefix[idx]
        total = (total + (q % mod) * (sum_h % mod)) % mod

    return total


if __name__ == "__main__":
    print(solve())
