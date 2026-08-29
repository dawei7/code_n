"""Project Euler 266: Pseudo Square Root

Find PSR(p) mod 10^16, where p is the product of all prime numbers below 190.
"""

from __future__ import annotations

import bisect
import math


def solve(max_prime: int = 190) -> str:
    """Finds the pseudo square root PSR(p) mod 10^16 using logarithmic meet-in-the-middle

    subset-product optimization over the prime factors below `max_prime`.
    """
    # Generate all prime numbers below max_prime
    sieve = [True] * max_prime
    primes: list[int] = []
    for p in range(2, max_prime):
        if sieve[p]:
            primes.append(p)
            for mult in range(p * p, max_prime, p):
                sieve[mult] = False

    logs = [math.log(p) for p in primes]
    total_log = sum(logs)
    target_log = total_log / 2.0

    # Split primes into two halves for meet-in-the-middle
    mid = len(primes) // 2
    primes_a, logs_a = primes[:mid], logs[:mid]
    primes_b, logs_b = primes[mid:], logs[mid:]

    # 1. Enumerate all subset products for half A
    list_a: list[tuple[float, int]] = [(0.0, 1)]
    for p, lp in zip(primes_a, logs_a):
        new_items = [(s + lp, prod * p) for s, prod in list_a]
        list_a.extend(new_items)

    list_a.sort(key=lambda x: x[0])
    logs_a_sorted = [x[0] for x in list_a]

    # 2. Enumerate all subset products for half B and query against A
    list_b: list[tuple[float, int]] = [(0.0, 1)]
    for p, lp in zip(primes_b, logs_b):
        new_items = [(s + lp, prod * p) for s, prod in list_b]
        list_b.extend(new_items)

    best_log = 0.0
    best_prod = 1

    for s_b, prod_b in list_b:
        rem_log = target_log - s_b
        if rem_log >= 0.0:
            idx = bisect.bisect_right(logs_a_sorted, rem_log) - 1
            if idx >= 0:
                s_a, prod_a = list_a[idx]
                curr_log = s_a + s_b
                if curr_log > best_log:
                    best_log = curr_log
                    best_prod = prod_a * prod_b

    ans = best_prod % (10**16)
    return str(ans)


if __name__ == "__main__":
    print(solve())
