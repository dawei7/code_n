"""Project Euler 326: Modulo Summations

Find f(10^12, 10^6), where f(N, M) represents the number of pairs (p, q)
such that 1 <= p <= q <= N and (sum_{i=p}^q a_i) mod M == 0.
"""

from __future__ import annotations


def solve(n: int = 1_000_000_000_000, m: int = 1_000_000) -> str:
    """Calculates f(n, m) using the fundamental 6M periodicity theorem of the prefix sums

    P_k = (sum_{i=1}^k a_i) mod m and frequency bucketing across quotient blocks.
    """
    period = 6 * m

    counts_full = [0] * m
    counts_rem = [0] * m

    r_rem = n % period
    num_full = n // period

    # Initial state: P_0 = 0
    p_cur = 0
    counts_full[0] += 1
    if r_rem >= 0:
        counts_rem[0] += 1

    s_acc = 1
    # Step n = 1: a_1 = 1
    p_cur = 1 % m
    counts_full[p_cur] += 1
    if r_rem >= 1:
        counts_rem[p_cur] += 1

    # Generate the remaining period n = 2 .. period
    for i in range(2, period + 1):
        a_i = s_acc % i
        s_acc += i * a_i
        p_cur = (p_cur + a_i) % m

        if i < period:
            counts_full[p_cur] += 1
        if i <= r_rem:
            counts_rem[p_cur] += 1

    # Aggregate matching pairs from prefix sum collisions: binom(Count(r), 2)
    total_pairs = 0
    for r in range(m):
        tot_cnt = num_full * counts_full[r] + counts_rem[r]
        total_pairs += tot_cnt * (tot_cnt - 1) // 2

    return str(total_pairs)


if __name__ == "__main__":
    print(solve())
