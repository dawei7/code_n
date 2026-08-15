"""Project Euler Problem 528: Constrained Sums.

Find sum_{k=10..15} S(10^k, k, k) mod 1_000_000_007, where S(n, k, b) is the number
of integer solutions to x_1 + ... + x_k <= n with 0 <= x_m <= b^m.
"""

from typing import List

MOD = 1_000_000_007


def _comb_mod(n: int, k: int) -> int:
    if n < k or k < 0:
        return 0
    num = 1
    den = 1
    for i in range(1, k + 1):
        num = (num * ((n - i + 1) % MOD)) % MOD
        den = (den * i) % MOD
    return (num * pow(den, MOD - 2, MOD)) % MOD


def s_constrained(n: int, k: int, b: int) -> int:
    """Compute S(n, k, b) mod MOD using Principle of Inclusion-Exclusion over 2^k subsets."""
    weights: List[int] = [pow(b, m) + 1 for m in range(1, k + 1)]
    total = 0

    for mask in range(1 << k):
        shift = 0
        sign = 1
        for i in range(k):
            if (mask >> i) & 1:
                shift += weights[i]
                sign = -sign
        rem = n - shift
        if rem >= 0:
            total = (total + sign * _comb_mod(rem + k, k)) % MOD

    return total % MOD


def solve(k_min: int = 10, k_max: int = 15, mod: int = MOD) -> int:
    """Compute sum_{k=k_min..k_max} S(10^k, k, k) mod mod."""
    total = 0
    for k in range(k_min, k_max + 1):
        total = (total + s_constrained(pow(10, k), k, k)) % mod
    return total


if __name__ == "__main__":
    print(solve())
