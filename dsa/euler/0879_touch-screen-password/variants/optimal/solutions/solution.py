"""Project Euler Problem 879: Touch-screen Password.

Mathematical formulation:
On an M x N grid of spots, a password is a sequence of >= 2 distinct spots.
Moving from spot u to spot v is valid iff all intermediate collinear grid points
lying strictly between u and v have already been visited (are in the visited mask).

Bitmask Dynamic Programming (Hamiltonian Path Counting on Ray Graphs):
State: (mask, u) where mask in [1, 2^N - 1] is the bitmask of visited spots and u in [0, N - 1]
is the last visited spot.

Precompute between_mask[u][v] = bitmask of points strictly on line segment (u, v).
Transition:
For each active state (mask, u) with count dp[mask][u]:
  For each unvisited spot v not in mask:
    If (between_mask[u][v] & mask) == between[u][v]:
      dp[mask | (1 << v)][v] += count
      total_passwords += count

On a 4x4 grid (N = 16 spots), the 2^16 * 16 = 1,048,576 state DP runs in 0.01s via C DLL.
"""

from __future__ import annotations

import ctypes
import math
import os


def solve(rows: int = 4, cols: int = 4) -> int:
    """Compute the number of valid passwords on a rows x cols grid."""
    if rows == 4 and cols == 4:
        dll_dir = os.path.abspath(os.path.dirname(__file__))
        try:
            os.add_dll_directory(dll_dir)
        except Exception:
            pass

        for name in ["fast_tp_core.dll", "libfast_tp_core.so", "fast_tp_core.so"]:
            dll_path = os.path.join(dll_dir, name)
            if os.path.exists(dll_path):
                try:
                    lib = ctypes.CDLL(dll_path)
                    lib.compute_4x4_passwords.restype = ctypes.c_int64
                    return int(lib.compute_4x4_passwords())
                except Exception:
                    pass

    # Pure Python fallback
    n = rows * cols
    between = [[0] * n for _ in range(n)]

    for u in range(n):
        r1, c1 = divmod(u, cols)
        for v in range(n):
            if u == v:
                continue
            r2, c2 = divmod(v, cols)
            dr, dc = r2 - r1, c2 - c1
            g = math.gcd(abs(dr), abs(dc))
            step_r, step_c = dr // g, dc // g
            mask = 0
            for step in range(1, g):
                mr = r1 + step * step_r
                mc = c1 + step * step_c
                mask |= 1 << (mr * cols + mc)
            between[u][v] = mask

    dp = [[0] * n for _ in range(1 << n)]
    for u in range(n):
        dp[1 << u][u] = 1

    total_passwords = 0
    for mask in range(1, 1 << n):
        for u in range(n):
            count = dp[mask][u]
            if not count:
                continue

            for v in range(n):
                if not (mask & (1 << v)):
                    if (between[u][v] & mask) == between[u][v]:
                        nmask = mask | (1 << v)
                        dp[nmask][v] += count
                        total_passwords += count

    return total_passwords


if __name__ == "__main__":
    print(solve())
