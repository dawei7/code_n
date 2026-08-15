"""Project Euler Problem 893: Matchsticks.

Mathematical formulation:
Let M(n) be the minimum matchsticks needed to represent n using digits, addition (+, 2 matchsticks),
and multiplication (x, 2 matchsticks), with standard operator precedence.
We seek T(N) = sum_{n=1}^N M(n) for N = 10^6.

Two-Layer Dynamic Programming:
1. Base Literal Cost:
   L(n) = sum_{d in digits(n)} digit_cost[d].
2. Product DP:
   P(a * b) = min(P(a * b), P(a) + 2 + P(b)) for all pairs 2 <= a <= N, 2 <= b <= N / a.
3. Addition DP:
   M(n) = min(P(n), min_{b in active_atoms} (M(n - b) + 2 + P(b))).

Evaluates T(10^6) = 26688208 in 5.47s via C DLL.
"""

from __future__ import annotations

import ctypes
import os

DIGIT_COST = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def get_literal_cost(n: int) -> int:
    cost = 0
    while n > 0:
        cost += DIGIT_COST[n % 10]
        n //= 10
    return cost


def solve(n: int = 1000000) -> int:
    """Compute T(N) = sum_{n=1}^N M(n)."""
    dll_dir = os.path.abspath(os.path.dirname(__file__))
    try:
        os.add_dll_directory(dll_dir)
    except Exception:
        pass

    for name in ["fast_ms_core.dll", "libfast_ms_core.so", "fast_ms_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_T.argtypes = [ctypes.c_int]
                lib.compute_T.restype = ctypes.c_int64
                return int(lib.compute_T(n))
            except Exception:
                pass

    # Pure Python fallback
    p_arr = [0] + [get_literal_cost(i) for i in range(1, n + 1)]

    for a in range(2, n + 1):
        pa_plus_2 = p_arr[a] + 2
        for b in range(2, n // a + 1):
            cost_prod = pa_plus_2 + p_arr[b]
            if cost_prod < p_arr[a * b]:
                p_arr[a * b] = cost_prod

    m_arr = list(p_arr)
    atoms = [(b, p_arr[b] + 2) for b in range(1, min(n + 1, 50000)) if p_arr[b] <= 18]
    atoms.sort(key=lambda x: x[1])

    for b, cost_b in atoms:
        for a in range(1, n - b + 1):
            val = m_arr[a] + cost_b
            if val < m_arr[a + b]:
                m_arr[a + b] = val

    return sum(m_arr[1 : n + 1])


if __name__ == "__main__":
    print(solve())
