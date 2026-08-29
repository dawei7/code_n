"""Project Euler 341: Golomb's Self-describing Sequence

Find sum_{n=1}^{10^6 - 1} G(n^3), where G(n) is Golomb's self-describing sequence.
"""

from __future__ import annotations


def solve(max_n: int = 1_000_000, v_max: int = 8_000_000) -> str:
    """Calculates sum_{n=1}^{max_n - 1} G(n^3) in pure Python in O(V_max + max_n) time

    using hierarchical block-sum prefix advances and two-pointer interval stepping.
    """
    # 1. Generate Golomb sequence G array up to V_max
    g = [0] * (v_max + 1)
    g[1] = 1
    g[2] = 2
    g[3] = 2
    curr = 4
    for val in range(3, v_max + 1):
        count = g[val]
        for _ in range(count):
            if curr > v_max:
                break
            g[curr] = val
            curr += 1
        if curr > v_max:
            break

    # 2. Advance through blocks of value v and answer monotonic queries n^3
    total_sum = 0
    n = 1
    target = 1  # 1^3

    k_start = 0
    s_start = 0

    for v in range(1, v_max + 1):
        g_v = g[v]
        if g_v == 0:
            break
        s_end = s_start + v * g_v

        while n < max_n and target <= s_end:
            # Query target falls in current block of value v
            rem = target - s_start
            j = (rem + v - 1) // v
            k = k_start + j
            total_sum += k
            n += 1
            target = n * n * n

        if n >= max_n:
            break

        k_start += g_v
        s_start = s_end

    return str(total_sum)


if __name__ == "__main__":
    print(solve())
