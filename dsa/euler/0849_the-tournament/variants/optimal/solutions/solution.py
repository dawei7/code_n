"""Project Euler Problem 849: The Tournament.

Mathematical formulation:
A sequence 0 <= s_1 <= s_2 <= ... <= s_n is a valid score sequence for a double round-robin tournament
(where each pair of teams plays twice, with sum of scores = 4 per pair) if and only if
by Landau's Theorem for multigraph tournaments:
  sum_{i=1}^m s_i >= 2*m*(m - 1)  for all 1 <= m < n
  sum_{i=1}^n s_i = 2*n*(n - 1)

Dynamic Programming by Score Value:
Iterate score values v from 0 to 4*(n - 1).
Maintain state (M, E) where:
  - M in [0, n] is the number of teams assigned a score <= v
  - E = S_M - 2*M*(M - 1) >= 0 is the current Landau excess

When adding k teams with score v:
  - new_M = M + k
  - new_E = E + k * (v - 4*M - 2*k + 2) >= 0

For n = 100, max_E <= 5000, leading to a state space of (100 * 5000) evaluated over 396 steps.
Implemented via compiled C DLL with pure Python fallback.
"""

from __future__ import annotations

import ctypes
import os


def solve(n: int = 100, modulo: int = 1000000007) -> int:
    """Compute F(n) modulo 10^9 + 7."""
    dll_dir = os.path.dirname(__file__)
    for name in ["fast_tourn_core.dll", "libfast_tourn_core.so", "fast_tourn_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_tournament_outcomes.argtypes = [ctypes.c_int]
                lib.compute_tournament_outcomes.restype = ctypes.c_int
                return int(lib.compute_tournament_outcomes(n))
            except Exception:
                pass

    # Pure Python fallback
    max_v = 4 * (n - 1)
    dp: dict[tuple[int, int], int] = {(0, 0): 1}

    for v in range(0, max_v + 1):
        next_dp: dict[tuple[int, int], int] = {}
        for (m, e), ways in dp.items():
            # k = 0
            next_dp[(m, e)] = (next_dp.get((m, e), 0) + ways) % modulo
            # k >= 1
            for k in range(1, n - m + 1):
                new_m = m + k
                delta_e = k * (v - 4 * m - 2 * k + 2)
                new_e = e + delta_e
                if new_e >= 0:
                    next_dp[(new_m, new_e)] = (next_dp.get((new_m, new_e), 0) + ways) % modulo
        dp = next_dp

    return dp.get((n, 0), 0)


if __name__ == "__main__":
    print(solve())
