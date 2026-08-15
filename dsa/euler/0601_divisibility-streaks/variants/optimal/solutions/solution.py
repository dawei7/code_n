"""Project Euler Problem 601: Divisibility Streaks.

Find sum_{i=1}^{31} P(i, 4^i), where P(s, N) is the count of 1 < n < N with streak(n) = s.
"""

import math
from typing import List


def _compute_lcm_table(max_s: int) -> List[int]:
    lcm_table = [1] * (max_s + 2)
    curr = 1
    for i in range(1, max_s + 2):
        curr = (curr * i) // math.gcd(curr, i)
        lcm_table[i] = curr
    return lcm_table


def _p_func(s: int, n_limit: int, lcm_table: List[int]) -> int:
    return (n_limit - 2) // lcm_table[s] - (n_limit - 2) // lcm_table[s + 1]


def solve(max_i: int = 31) -> int:
    """Compute sum of P(i, 4^i) for 1 <= i <= max_i using prefix LCM intervals."""
    lcm_table = _compute_lcm_table(max_i)
    total = 0
    for i in range(1, max_i + 1):
        n_limit = 4**i
        total += _p_func(i, n_limit, lcm_table)
    return total


if __name__ == "__main__":
    print(solve())
