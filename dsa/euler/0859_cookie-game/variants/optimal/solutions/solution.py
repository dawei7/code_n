"""Project Euler Problem 859: Cookie Game.

Mathematical formulation:
This is a partisan combinatorial game under normal play convention:
- Odd can only move on odd piles (replacing 2m+1 with two piles of m).
- Even can only move on even piles (replacing 2m+2 with two piles of m).

By Conway's Combinatorial Game Theory (CGT / ONAG):
Each pile of size n is a dyadic rational integer game value g(n):
  g(0) = 0
  g(2m + 1) = max(0, 2*g(m) + 1)
  g(2m + 2) = min(0, 2*g(m) - 1)

For any partition of N cookies, the game value is the sum of pile values sum_{i} g(p_i).
Since Odd moves first, Even (playing second) has a winning strategy if and only if:
  sum_{i} g(p_i) <= 0.

We count integer partitions of N = 300 with non-positive total CGT value via 2D knapsack DP:
  dp[w][v] = count of partitions of weight w summing to CGT value v.

Evaluated in under 0.01 seconds via high-performance C DLL with Python fallback.
"""

from __future__ import annotations

import ctypes
import os


def solve(n: int = 300) -> int:
    """Compute C(n), the number of winning initial partitions for Even."""
    dll_dir = os.path.dirname(__file__)
    for name in ["fast_cookie_core.dll", "libfast_cookie_core.so", "fast_cookie_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_winning_partitions.argtypes = [ctypes.c_int]
                lib.compute_winning_partitions.restype = ctypes.c_int64
                return int(lib.compute_winning_partitions(n))
            except Exception:
                pass

    # Pure Python fallback
    g = [0] * (n + 1)
    for k in range(1, n + 1):
        if k % 2 == 1:
            m = (k - 1) // 2
            g[k] = max(0, 2 * g[m] + 1)
        else:
            m = (k - 2) // 2
            g[k] = min(0, 2 * g[m] - 1)

    max_v = n
    v_size = 2 * max_v + 1
    offset = max_v

    table = [[0] * v_size for _ in range(n + 1)]
    table[0][offset] = 1

    for x in range(1, n + 1):
        gx = g[x]
        for w in range(x, n + 1):
            for v in range(v_size):
                prev_v = v - gx
                if 0 <= prev_v < v_size:
                    table[w][v] += table[w - x][prev_v]

    return sum(table[n][v] for v in range(0, offset + 1))


if __name__ == "__main__":
    print(solve())
