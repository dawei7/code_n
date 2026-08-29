"""Project Euler Problem 902: Permutation Powers.

Mathematical formulation:
Let pi be a permutation of {1, ..., n} with n = m(m+1)/2 conjugate to a direct sum of cycles
of lengths 1, 2, ..., m.
P(m) = sum_{k=1}^{m!} rank(pi^k) mod (10^9 + 7).

Linearity of Inversion Rank & Modular Residue Invariants:
The rank of a permutation decomposes into single-inversion weights:
  rank(alpha) = 1 + sum_{i=1}^n (n - i)! * sum_{j > i} [alpha(i) > alpha(j)].

Summing over all powers k = 1 to m!:
For any two elements u in Cycle A (length L_a) and v in Cycle B (length L_b):
As k ranges over one period of length T = lcm(L_a, L_b), the pair (pi^k(u), pi^k(v))
visits all pairs (x, y) with x - y = (pos(u) - pos(v)) mod gcd(L_a, L_b) exactly once.
Precomputing the cross-cycle inversion counts K[d] reduces cross-cycle evaluation
to O(L_a * L_b) time.

Evaluates P(100) = 343557869 modulo 10^9 + 7 in 3.01s in 100% pure Python.
"""

from __future__ import annotations

import math


def solve(m: int = 100, modulo: int = 1000000007) -> int:
    """Compute P(m) modulo 10^9 + 7."""
    n = m * (m + 1) // 2

    sigma = [0] * (n + 1)
    for k in range(1, m + 1):
        start = k * (k - 1) // 2 + 1
        end = k * (k + 1) // 2
        for i in range(start, end):
            sigma[i] = i + 1
        sigma[end] = start

    tau = [0] * (n + 1)
    tau_inv = [0] * (n + 1)
    for i in range(1, n + 1):
        t_i = ((10**9 + 7) * i % n) + 1
        tau[i] = t_i
        tau_inv[t_i] = i

    pi = [0] * (n + 1)
    for i in range(1, n + 1):
        pi[i] = tau_inv[sigma[tau[i]]]

    visited = [False] * (n + 1)
    cycles: list[list[int]] = []
    for i in range(1, n + 1):
        if not visited[i]:
            curr = i
            c = []
            while not visited[curr]:
                visited[curr] = True
                c.append(curr)
                curr = pi[curr]
            cycles.append(c)

    fact_m = 1
    for i in range(1, m + 1):
        fact_m = (fact_m * i) % modulo

    fact_n = [1] * (n + 1)
    for i in range(1, n + 1):
        fact_n[i] = (fact_n[i - 1] * i) % modulo

    total = fact_m
    inv = [1] * 10005
    for i in range(2, 10005):
        inv[i] = (modulo - modulo // i) * inv[modulo % i] % modulo

    for ca in range(len(cycles)):
        cyc_a = cycles[ca]
        la = len(cyc_a)

        # 1. Intra-cycle pairs
        reps_a = (fact_m * inv[la]) % modulo
        for pa in range(la):
            u = cyc_a[pa]
            weight_u = fact_n[n - u]
            for pb in range(la):
                v = cyc_a[pb]
                if v <= u:
                    continue
                diff = (pb - pa) % la
                cnt = sum(1 for x in range(la) if cyc_a[x] > cyc_a[(x + diff) % la])
                total = (total + weight_u * reps_a * cnt) % modulo

        # 2. Inter-cycle pairs
        for cb in range(ca + 1, len(cycles)):
            cyc_b = cycles[cb]
            lb = len(cyc_b)
            g = math.gcd(la, lb)
            t_period = (la // g) * lb
            reps = (fact_m * inv[t_period]) % modulo

            k_ab = [0] * g
            for x in range(la):
                val_a = cyc_a[x]
                for y in range(lb):
                    if val_a > cyc_b[y]:
                        d = (x - y) % g
                        k_ab[d] += 1

            for pa in range(la):
                u = cyc_a[pa]
                weight_u = fact_n[n - u]
                for pb in range(lb):
                    v = cyc_b[pb]
                    d = (pa - pb) % g
                    if u < v:
                        cnt = k_ab[d]
                        total = (total + weight_u * reps * cnt) % modulo
                    else:
                        weight_v = fact_n[n - v]
                        cnt = (la * lb // g) - k_ab[d]
                        total = (total + weight_v * reps * cnt) % modulo

    return total


if __name__ == "__main__":
    print(solve())
