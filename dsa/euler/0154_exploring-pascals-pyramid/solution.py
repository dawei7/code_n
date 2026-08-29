"""Project Euler 154: Exploring Pascal's Pyramid

Find the number of trinomial coefficients in (x+y+z)^N (N=200,000) divisible by 10^12 = 2^12 * 5^12.
"""

from __future__ import annotations


def solve(n: int = 200_000) -> str:
    """Calculates the number of trinomial coefficients divisible by 10^12 in pure Python

    using Kummer's theorem on multinomial p-adic valuations and base-5 / base-2 digit sums:
    v_5(N! / (i! j! k!)) = (S_5(i) + S_5(j) + S_5(k) - S_5(N)) / 4 >= 12 <=> S_5(i) + S_5(j) + S_5(k) >= 56
    v_2(N! / (i! j! k!)) = S_2(i) + S_2(j) + S_2(k) - S_2(N) >= 12 <=> S_2(i) + S_2(j) + S_2(k) >= 18
    where i + j + k = N and 0 <= i <= j <= k.
    """
    # 1. Precompute base-5 digit sum S_5(x) and base-2 popcount S_2(x)
    s5 = [0] * (n + 1)
    s2 = [0] * (n + 1)
    for x in range(1, n + 1):
        s5[x] = s5[x // 5] + (x % 5)
        s2[x] = s2[x >> 1] + (x & 1)

    s5_n = s5[n]  # S_5(200000) = 8
    s2_n = s2[n]  # S_2(200000) = 6
    min_s5 = 48 + s5_n  # 56
    min_s2 = 12 + s2_n  # 18

    # 2. Iterate canonical representative partitions 0 <= i <= j <= k = n - i - j
    count = 0
    max_i = n // 3

    for i in range(max_i + 1):
        s5_i = s5[i]
        req_5 = min_s5 - s5_i
        if req_5 > 56:  # Max possible sum of two numbers <= 200000 is 28 + 28 = 56
            continue
        s2_i = s2[i]
        req_2 = min_s2 - s2_i

        m = n - i
        max_j = m // 2
        for j in range(i, max_j + 1):
            k = m - j
            if s5[j] + s5[k] >= req_5 and s2[j] + s2[k] >= req_2:
                if i == j == k:
                    count += 1
                elif i == j or j == k or i == k:
                    count += 3
                else:
                    count += 6

    return str(count)


if __name__ == "__main__":
    print(solve())
