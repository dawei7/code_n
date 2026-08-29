"""Project Euler 254: Sums of Digit Factorials

Find sum_{i=1}^{150} sg(i), where:
f(n) is the sum of the factorials of the digits of n.
sf(n) is the sum of the digits of f(n).
g(i) is the smallest positive integer such that sf(n) = i.
sg(i) is the sum of the digits of g(i).
"""

from __future__ import annotations

import math


def solve(max_i: int = 150) -> str:
    """Computes sum_{i=1}^{max_i} sg(i) using factoradic canonical prefixes

    and exact digit-sum inversion.
    """
    fact = [math.factorial(i) for i in range(10)]
    fact9 = fact[9]

    # Precompute canonical prefix representations for all remainders R in [0, 9! - 1].
    # Any canonical integer n = P(R) 9^q has digits in non-decreasing order with at most
    # d digits equal to d for each d in 1..8.
    prefix_info: list[tuple[str, int, int] | None] = [None] * fact9
    for R in range(fact9):
        rem = R
        c = [0] * 9
        for d in range(8, 0, -1):
            c[d] = rem // fact[d]
            rem = rem % fact[d]
        s_digits = "".join(str(d) * c[d] for d in range(1, 9))
        d_sum = sum(d * c[d] for d in range(1, 9))
        prefix_info[R] = (s_digits, d_sum, len(s_digits))

    def cand_key(p_str: str, p_len: int, q: int) -> tuple[int, str]:
        pad = p_str + "9" * min(q, 40)
        return (p_len + q, pad)

    best: dict[int, tuple[tuple[int, str], str, int, int]] = {}

    # Exact search for small q (up to 85) across all factoradic remainders
    for q in range(85):
        q_fact9 = q * fact9
        for R in range(fact9):
            F = R + q_fact9
            if F == 0:
                continue
            temp = F
            s = 0
            while temp > 0:
                s += temp % 10
                temp //= 10
            if s <= 65:
                p_str, p_sum, p_len = prefix_info[R]
                key = cand_key(p_str, p_len, q)
                cand = (key, p_str, q, p_sum + 9 * q)
                if s not in best or cand[0] < best[s][0]:
                    best[s] = cand

    # Exact minimal integer decomposition for large i (i >= 64)
    # The minimal positive integer with digit sum i is unique:
    # F = (i % 9 + 1) * 10^(i // 9) - 1 (or 10^(i // 9) - 1 when i % 9 == 0).
    for i in range(64, max_i + 1):
        r = i % 9
        k = i // 9
        if r > 0:
            F = (r + 1) * (10**k) - 1
        else:
            F = 10**k - 1
        R = F % fact9
        q = F // fact9
        p_str, p_sum, p_len = prefix_info[R]
        key = cand_key(p_str, p_len, q)
        cand = (key, p_str, q, p_sum + 9 * q)
        if i not in best or cand[0] < best[i][0]:
            best[i] = cand

    total_sg = sum(best[i][3] for i in range(1, max_i + 1))
    return str(total_sg)


if __name__ == "__main__":
    print(solve())
