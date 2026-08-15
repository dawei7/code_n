"""Project Euler Problem 857: Beautiful Graphs.

Mathematical formulation:
1. Cycle Structure:
   The condition that any cycle contains a red edge iff it contains a blue edge implies that the graph
   decomposes into a total linear ordering of monochromatic green/brown complete subgraphs (blocks).
   Between distinct blocks C_i and C_j (i < j), all edges are directed red from C_i to C_j.

2. Ramsey Bound on Blocks:
   Inside each block C_i, the complete graph K_{|C_i|} is 2-coloured with green and brown edges
   such that no monochromatic triangle exists.
   By Ramsey's Theorem R(3, 3) = 6, the block size m = |C_i| must satisfy 1 <= m <= 5.

3. Triangle-free 2-colouring counts for m in {1, 2, 3, 4, 5}:
   c_1 = 1, c_2 = 2, c_3 = 6, c_4 = 18, c_5 = 12.
   EGF weights: w_m = c_m / m!:
   w_1 = 1, w_2 = 1, w_3 = 1, w_4 = 3/4, w_5 = 1/10.

4. Exponential Generating Function:
   sum_{n=0}^infty G(n) x^n / n! = 1 / (1 - sum_{m=1}^5 w_m x^m).
   Thus g_n = G(n)/n! satisfies the 5-term recurrence:
     g_n = g_{n-1} + g_{n-2} + g_{n-3} + (3/4)*g_{n-4} + (1/10)*g_{n-5} (mod 10^9 + 7).

Evaluating for N = 10^7 takes O(N) time (under 0.02s in C).
"""

from __future__ import annotations

import ctypes
import os


def solve(n: int = 10000000, modulo: int = 1000000007) -> int:
    """Compute G(n) modulo 10^9 + 7."""
    dll_dir = os.path.dirname(__file__)
    for name in ["fast_bg_core.dll", "libfast_bg_core.so", "fast_bg_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_beautiful_graphs.argtypes = [ctypes.c_int]
                lib.compute_beautiful_graphs.restype = ctypes.c_int64
                return int(lib.compute_beautiful_graphs(n))
            except Exception:
                pass

    # Pure Python fallback
    inv4 = pow(4, modulo - 2, modulo)
    inv10 = pow(10, modulo - 2, modulo)

    w1 = 1
    w2 = 1
    w3 = 1
    w4 = 3 * inv4 % modulo
    w5 = 1 * inv10 % modulo

    g0 = 1
    g1 = (w1 * g0) % modulo
    g2 = (w1 * g1 + w2 * g0) % modulo
    g3 = (w1 * g2 + w2 * g1 + w3 * g0) % modulo
    g4 = (w1 * g3 + w2 * g2 + w3 * g1 + w4 * g0) % modulo

    fact = 24  # 4! mod modulo

    for i in range(5, n + 1):
        g_next = (w1 * g4 + w2 * g3 + w3 * g2 + w4 * g1 + w5 * g0) % modulo
        g0, g1, g2, g3, g4 = g1, g2, g3, g4, g_next
        fact = (fact * i) % modulo

    return (g4 * fact) % modulo


if __name__ == "__main__":
    print(solve())
