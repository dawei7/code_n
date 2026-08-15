"""Project Euler Problem 633: Square Prime Factors II.

Find the asymptotic density c_7^inf in scientific notation rounded to 5 significant digits.
"""

import math
from typing import List


def _sieve_primes(limit: int) -> List[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    primes: List[int] = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return primes


def solve(k_target: int = 7) -> str:
    """Compute asymptotic density c_k^inf using Prime Zeta logarithmic series exponentiation."""
    primes = _sieve_primes(1_000_000)

    a_coeffs = [0.0] * (k_target + 1)
    for p in primes:
        val = 1.0 / (p * p - 1)
        curr = val
        for m in range(1, k_target + 1):
            a_coeffs[m] += curr
            curr *= val

    g = [0.0] * (k_target + 1)
    g[0] = 6.0 / (math.pi**2)

    for n in range(1, k_target + 1):
        s = 0.0
        for m in range(1, n + 1):
            sign = 1.0 if (m % 2 == 1) else -1.0
            term = sign * a_coeffs[m] * g[n - m]
            s += term
        g[n] = s / n

    val = g[k_target]
    s_val = f"{val:.4e}"
    mantissa, exp = s_val.split("e")
    exp_int = int(exp)
    return f"{mantissa}e{exp_int}"


if __name__ == "__main__":
    print(solve())
