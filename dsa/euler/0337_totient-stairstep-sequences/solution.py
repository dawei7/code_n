"""Project Euler 337: Totient Stairstep Sequences

Find S(20000000) mod 10^8, where S(N) is the number of sequences
starting with a_1 = 6 and satisfying phi(a_i) < phi(a_{i+1}) < a_i < a_{i+1} with a_n <= N.
"""

from __future__ import annotations


def solve(limit: int = 20_000_000, mod: int = 100_000_000) -> str:
    """Calculates S(limit) mod mod in pure Python using a totient linear sieve

    and 1D Fenwick tree (Binary Indexed Tree) reduction:
    dp[y] = (FenwickQuery(phi(y) - 1) - pref_dp[phi(y)]) mod mod.
    """
    # 1. Euler's totient function sieve up to limit
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i

    # 2. 1D Fenwick Tree (Binary Indexed Tree) and Prefix DP arrays
    bit = [0] * (limit + 1)
    pref_dp = [0] * (limit + 1)

    # Base case: a_1 = 6 (dp[6] = 1, phi(6) = 2)
    pref_dp[6] = 1
    idx = phi[6]
    while idx <= limit:
        bit[idx] = (bit[idx] + 1) % mod
        idx += idx & (-idx)

    # 3. Dynamic programming transitions using 1D Fenwick query
    for y in range(7, limit + 1):
        py = phi[y]

        # Query prefix sum in Fenwick tree for all x < y with phi(x) <= py - 1
        q_idx = py - 1
        sum_query = 0
        while q_idx > 0:
            sum_query = (sum_query + bit[q_idx]) % mod
            q_idx -= q_idx & (-q_idx)

        # Subtract elements with x <= py (which all satisfy phi(x) < py)
        val = (sum_query - pref_dp[py]) % mod
        pref_dp[y] = (pref_dp[y - 1] + val) % mod

        # Insert dp[y] into Fenwick tree at position py
        a_idx = py
        while a_idx <= limit:
            bit[a_idx] = (bit[a_idx] + val) % mod
            a_idx += a_idx & (-a_idx)

    return str(pref_dp[limit])


if __name__ == "__main__":
    print(solve())
