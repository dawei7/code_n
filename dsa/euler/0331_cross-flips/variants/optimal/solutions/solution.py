"""Project Euler 331: Cross Flips

Find sum_{i=3}^{31} T(2^i - i), where T(N) is the minimal number of turns
to solve the cross-flips game on configuration C_N.
"""

from __future__ import annotations


def compute_t_even(n: int) -> int:
    """Computes T(N) for an even board size N in pure Python using a two-pointer

    circle boundary walk and prefix parity sums.
    """
    n1_sq = (n - 1) * (n - 1)
    n_sq_1 = n * n - 1

    y_max = n - 1
    y_min = n - 1

    r = [0] * n
    y_min_arr = [0] * n
    y_max_arr = [0] * n

    for x in range(n):
        x2 = x * x
        while y_max >= 0 and x2 + y_max * y_max > n_sq_1:
            y_max -= 1
        while y_min > 0 and x2 + (y_min - 1) * (y_min - 1) >= n1_sq:
            y_min -= 1
        y_max_arr[x] = y_max
        y_min_arr[x] = y_min
        if y_max >= y_min:
            r[x] = (y_max - y_min + 1) & 1

    if sum(r) & 1:
        for x in range(n):
            r[x] ^= 1

    c1 = sum(r)
    c0 = n - c1

    pref_r = [0] * (n + 1)
    for i in range(n):
        pref_r[i + 1] = pref_r[i] + r[i]

    black_same = 0
    black_diff = 0
    for x in range(n):
        ym = y_min_arr[x]
        ym_max = y_max_arr[x]
        if ym_max >= ym:
            ones = pref_r[ym_max + 1] - pref_r[ym]
            zeros = (ym_max - ym + 1) - ones
            if r[x] == 1:
                black_same += ones
                black_diff += zeros
            else:
                black_same += zeros
                black_diff += ones

    return 2 * c0 * c1 + black_same - black_diff


def solve(min_i: int = 3, max_i: int = 31) -> str:
    """Calculates sum_{i=min_i}^{max_i} T(2^i - i) in pure Python using linear algebra over GF(2),

    the odd-parity unsolvability theorem (T(2^i - i) = 0 for odd i >= 5),
    and two-pointer digital circle boundary evaluation for even N.
    """
    total_turns = 0

    for i in range(min_i, max_i + 1):
        if i == 3:
            # N = 5 has unique solution T(5) = 3
            total_turns += 3
        elif i % 2 == 1:
            # All odd i >= 5 have inhomogeneous row parities => unsolvable T(N) = 0
            continue
        else:
            # Even N = 2^i - i
            n = (1 << i) - i
            turns = compute_t_even(n)
            total_turns += turns

    return str(total_turns)


if __name__ == "__main__":
    print(solve())
