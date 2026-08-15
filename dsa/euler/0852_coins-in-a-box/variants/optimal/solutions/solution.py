"""Project Euler Problem 852: Coins in a Box.

Mathematical formulation:
Let V(u, f) be the optimal expected score when u unfair coins (P(H)=0.75) and f fair coins (P(H)=0.5)
remain in the box.

Upon drawing a coin with prior p = u / (u + f):
1. The within-round optimal stopping problem on the head/tail tree (h, t):
   A(h, t) = u * (0.75)^h * (0.25)^t
   B(h, t) = f * (0.5)^(h + t)
   StopVal(h, t) = max(20*A - 50*B, 20*B - 50*A)
   ContVal(h, t) = -(A + B) + J(h + 1, t) + J(h, t + 1)
   J(h, t) = max(StopVal, ContVal) evaluated backwards from max_flips = 200.
   Single-round expected value: W(u, f) = J(0, 0) / (u + f).

2. Dynamic programming for the full game:
   V(u, f) = W(u, f) + [u * V(u - 1, f) + f * V(u, f - 1)] / (u + f)
   with base cases V(0, 0) = 0.

Implemented with high-performance C DLL and Python fallback.
"""

from __future__ import annotations

import ctypes
import os


def solve(n: int = 50) -> str:
    """Compute S(n) rounded to 6 digits after the decimal point."""
    dll_dir = os.path.dirname(__file__)
    for name in ["fast_box_core.dll", "libfast_box_core.so", "fast_box_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_expected_score.argtypes = [ctypes.c_int]
                lib.compute_expected_score.restype = ctypes.c_double
                ans = float(lib.compute_expected_score(n))
                return f"{ans:.6f}"
            except Exception:
                pass

    # Pure Python fallback
    max_flips = 180
    p34 = [0.75**i for i in range(max_flips + 1)]
    p14 = [0.25**i for i in range(max_flips + 1)]
    p12 = [0.5**i for i in range(2 * max_flips + 2)]

    def compute_w(u: int, f: int) -> float:
        j: dict[tuple[int, int], float] = {}
        for total in range(max_flips, -1, -1):
            for h in range(total + 1):
                t = total - h
                a = u * p34[h] * p14[t]
                b = f * p12[h + t]
                stop_val = max(20.0 * a - 50.0 * b, 20.0 * b - 50.0 * a)
                if total == max_flips:
                    j[(h, t)] = stop_val
                else:
                    cont_val = -(a + b) + j[(h + 1, t)] + j[(h, t + 1)]
                    j[(h, t)] = max(stop_val, cont_val)
        return j[(0, 0)] / (u + f)

    v: dict[tuple[int, int], float] = {}
    for total in range(2 * n + 1):
        for u in range(total + 1):
            f = total - u
            if u > n or f > n:
                continue
            if u == 0 and f == 0:
                v[(u, f)] = 0.0
                continue
            w = compute_w(u, f)
            future = 0.0
            if u > 0:
                future += u * v[(u - 1, f)]
            if f > 0:
                future += f * v[(u, f - 1)]
            future /= (u + f)
            v[(u, f)] = w + future

    return f"{v[(n, n)]:.6f}"


if __name__ == "__main__":
    print(solve())
