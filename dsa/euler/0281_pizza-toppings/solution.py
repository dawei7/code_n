"""Project Euler 281: Pizza Toppings

Find the sum of all f(m, n) <= 10^15, where f(m, n) denotes the number of ways
to place m different toppings on m * n equal pizza slices with each topping on
exactly n slices, considering rotations identical and reflections distinct.
"""

from __future__ import annotations

import math


def euler_phi(n: int) -> int:
    """Calculates Euler's totient function phi(n)."""
    res = n
    temp = n
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            res -= res // p
        p += 1
    if temp > 1:
        res -= res // temp
    return res


def f(m: int, n: int) -> int:
    """Calculates f(m, n) using Burnside's Lemma over the cyclic group C_{mn}."""
    total = 0
    for j in range(1, n + 1):
        if n % j == 0:
            coeff = euler_phi(n // j)
            term = math.factorial(j * m) // (math.factorial(j) ** m)
            total += coeff * term
    return total // (m * n)


def solve(limit: int = 10**15) -> str:
    """Calculates the sum of all f(m, n) <= limit for m >= 2, n >= 1."""
    total_sum = 0
    m = 2
    while True:
        n = 1
        val = f(m, n)
        if val > limit:
            break
        while True:
            val = f(m, n)
            if val > limit:
                break
            total_sum += val
            n += 1
        m += 1

    return str(total_sum)


if __name__ == "__main__":
    print(solve())
