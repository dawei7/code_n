"""Project Euler Problem 374: Maximum Integer Partition Product.

Find sum_{n=1..10^14} f(n) * m(n) mod 982451653, where f(n) is the maximum product of distinct
partitions of n and m(n) is the number of parts achieving that maximum.
"""

from math import isqrt
from typing import List


def solve(limit: int = 10**14, mod: int = 982451653) -> int:
    """Compute sum_{n=1..limit} f(n)*m(n) mod mod using optimal distinct partition intervals."""
    if limit <= 0:
        return 0
    if limit == 1:
        return 1 % mod
    if limit == 2:
        return (1 + 2) % mod
    if limit == 3:
        return (1 + 2 + 3) % mod
    if limit == 4:
        return (1 + 2 + 3 + 4) % mod

    inv2 = (mod + 1) // 2

    # Find k_max where T_k <= limit
    # T_k = (k+1)*(k+2)//2 - 1 = (k^2 + 3k)//2 <= limit
    k_max = (isqrt(9 + 8 * limit) - 3) // 2

    # Precompute modular inverse array up to k_max + 5 in O(k_max)
    inv: List[int] = [0] * (k_max + 5)
    inv[1] = 1
    for i in range(2, k_max + 5):
        inv[i] = (-(mod // i) * inv[mod % i]) % mod

    # Base sum for n = 1, 2, 3, 4
    total = 10 % mod

    fact = 6  # (2 + 1)! = 6
    h_sum = (inv[2] + inv[3]) % mod  # for k = 2: sum_{j=2..3} 1/j

    for k in range(2, k_max):
        bracket = (1 + (k + 3) * inv2 + (k + 2) * h_sum) % mod
        term = ((k * fact) % mod) * bracket % mod
        total = (total + term) % mod

        fact = (fact * (k + 2)) % mod
        h_sum = (h_sum + inv[k + 2]) % mod

    # Incomplete final interval at k = k_max
    k = k_max
    t_k = (k + 1) * (k + 2) // 2 - 1
    rem_count = limit - t_k

    if rem_count >= 0:
        total = (total + k * fact) % mod

    fact_k2 = (fact * (k + 2)) % mod
    max_r = min(k, rem_count)
    if max_r >= 1:
        sub_h = sum(inv[j] for j in range(k + 2 - max_r, k + 2)) % mod
        total = (total + ((k * fact_k2) % mod) * sub_h) % mod

    if rem_count >= k + 1:
        term_last = ((k * fact) % mod) * (((k + 3) * inv2) % mod) % mod
        total = (total + term_last) % mod

    return total % mod


if __name__ == "__main__":
    print(solve())
