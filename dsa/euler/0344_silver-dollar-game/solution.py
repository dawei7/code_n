"""Project Euler 344: Silver Dollar Game

Find W(1_000_000, 100) modulo the semiprime 1000_036_000_099 (= 1_000_003 * 1_000_033).
"""

from __future__ import annotations

import math


def solve(n: int = 1_000_000, c: int = 100, mod: int = 1_000_036_000_099) -> str:
    """Calculates W(n, c) mod M in pure Python in ~21s using Conway-Berlekamp Silver Dollar Game

    isomorphism, sparse binary generating functions, and linear modular binomials.
    """
    m = c // 2
    k = c + 1
    num_heaps = m + 1
    s_val = n - (c + 1)

    # 1. Compute counts of XOR=0 subsets via sparse binary polynomial multiplication
    def get_counts_array(m_heaps: int, max_s: int) -> list[int]:
        dp = [1]
        bits = max_s.bit_length()
        for bit in range(bits):
            shift = 1 << bit
            if shift > max_s:
                break
            terms = [
                (j * shift, math.comb(m_heaps, j) % mod)
                for j in range(0, m_heaps + 1, 2)
            ]
            new_len = min(max_s + 1, len(dp) + terms[-1][0])
            new_dp = [0] * new_len
            for j_shift, coeff in terms:
                for idx in range(len(dp)):
                    nxt = idx + j_shift
                    if nxt < new_len:
                        new_dp[nxt] = (new_dp[nxt] + dp[idx] * coeff) % mod
            dp = new_dp

        if len(dp) < max_s + 2:
            dp.extend([0] * (max_s + 2 - len(dp)))
        return dp[: max_s + 2]

    counts_51 = get_counts_array(num_heaps, s_val + 1)
    counts_50 = get_counts_array(num_heaps - 1, s_val + 1)

    # 2. Precompute binomial coefficients binom(rem + m, m) mod mod
    binom_arr = [0] * (s_val + 2)
    binom_arr[0] = 1
    for rem in range(1, s_val + 2):
        binom_arr[rem] = (
            binom_arr[rem - 1] * (rem + m) * pow(rem, -1, mod)
        ) % mod

    # 3. Sum losing positions L_1 (dollar at coin 1) and L_other (dollar at coins 2..c)
    l_1 = 0
    for h in range(s_val + 1):
        if counts_51[h]:
            l_1 = (l_1 + counts_51[h] * binom_arr[s_val - h]) % mod

    l_other = 0
    for h_prime in range(1, s_val + 2):
        diff = (counts_51[h_prime] - counts_50[h_prime]) % mod
        if diff:
            l_other = (
                l_other + diff * binom_arr[s_val - (h_prime - 1)]
            ) % mod

    total_l = (l_1 + (c - 1) * l_other) % mod

    # 4. Total all configurations: (c + 1) * binom(n, c + 1) mod mod
    num = 1
    den = 1
    for i in range(1, k + 1):
        num = (num * (n - i + 1)) % mod
        den = (den * i) % mod
    binom_n_k = (num * pow(den, -1, mod)) % mod
    total_all = (k * binom_n_k) % mod

    w_ans = (total_all - total_l) % mod
    return str(w_ans)


if __name__ == "__main__":
    print(solve())
