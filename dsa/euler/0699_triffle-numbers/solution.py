"""Project Euler Problem 699: Triffle Numbers.

Find T(10^14), the sum of all integers n <= N such that sigma(n)/n in lowest terms
has a denominator that is a positive power of 3 (b = 3^k, k > 0).
"""

import math
import random
import sys
from typing import Dict, List, Tuple


def _is_probable_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small_primes:
        if n % p == 0:
            return n == p

    d = n - 1
    s = 0
    while (d & 1) == 0:
        s += 1
        d >>= 1

    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def _pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    while True:
        c = random.randrange(1, n)
        x = random.randrange(0, n)
        y = x
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d


def _factorize(n: int, out: Dict[int, int]) -> None:
    if n == 1:
        return
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            cnt = 0
            while n % p == 0:
                n //= p
                cnt += 1
            out[p] = out.get(p, 0) + cnt
            if n == 1:
                return
            break

    if n == 1:
        return
    if _is_probable_prime(n):
        out[n] = out.get(n, 0) + 1
        return

    d = _pollard_rho(n)
    _factorize(d, out)
    _factorize(n // d, out)


def _factor_multiset(n: int) -> Dict[int, int]:
    res: Dict[int, int] = {}
    _factorize(n, res)
    return res


def _is_power_of_3(n: int) -> int:
    if n <= 0:
        return -1
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k if n == 1 else -1


def _sigma_prime_power(p: int, e: int) -> int:
    return (pow(p, e + 1) - 1) // (p - 1)


def _seed_states(limit: int) -> List[Tuple[int, int, int]]:
    pow2 = [1]
    while pow2[-1] * 2 <= limit:
        pow2.append(pow2[-1] * 2)
    pow3 = [1]
    while pow3[-1] * 3 <= limit:
        pow3.append(pow3[-1] * 3)
    pow5 = [1]
    while pow5[-1] * 5 <= limit:
        pow5.append(pow5[-1] * 5)

    seeds: List[Tuple[int, int, int]] = []
    for a, pa in enumerate(pow2):
        sig2 = (pa * 2 - 1) if a > 0 else 1
        for b in range(1, len(pow3)):
            pb = pow3[b]
            if pa * pb > limit:
                break
            sig3 = (pb * 3 - 1) // 2
            for c, pc in enumerate(pow5):
                val = pa * pb * pc
                if val > limit:
                    break
                sig5 = (pc * 5 - 1) // 4 if c > 0 else 1
                sig = sig2 * sig3 * sig5

                g = math.gcd(val, sig)
                num = sig // g
                den = val // g

                if den % 3 != 0 or den == 1:
                    continue

                seeds.append((val, num, den))
    return seeds


def solve(limit: int = 100_000_000_000_000) -> int:
    """Compute T(limit) using seed generation and prime cancellation DFS."""
    random.seed(0)
    sys.setrecursionlimit(2_000_000)

    fac_cache: Dict[int, Dict[int, int]] = {}

    def factors_of(x: int) -> Dict[int, int]:
        if x in fac_cache:
            return fac_cache[x]
        d = _factor_multiset(x)
        fac_cache[x] = d
        return d

    seeds = _seed_states(limit)
    visited = set()
    total = 0

    def dfs(cur_n: int, num: int, den: int) -> None:
        nonlocal total
        if cur_n in visited:
            return
        visited.add(cur_n)

        k = _is_power_of_3(den)
        if k > 0:
            total += cur_n

        if den == 1 or den % 3 != 0 or num == 1:
            return

        fac = factors_of(num)
        for p, exp in fac.items():
            if p <= 5 or cur_n % p == 0:
                continue

            pp = 1
            for e in range(1, exp + 1):
                pp *= p
                if cur_n > limit // pp:
                    break

                new_num = (num // pp) * _sigma_prime_power(p, e)
                new_den = den

                g = math.gcd(new_num, new_den)
                new_num //= g
                new_den //= g
                dfs(cur_n * pp, new_num, new_den)

    for val, num, den in seeds:
        dfs(val, num, den)

    return total


if __name__ == "__main__":
    print(solve())
