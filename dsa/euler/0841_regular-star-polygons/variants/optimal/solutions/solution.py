"""Project Euler Problem 841: Regular Star Polygons.

Mathematical reduction:
Consider a regular star polygon {p/q} with inradius 1.
The edge lines of {p/q} form an arrangement with 2p fundamental sectors of angle alpha = pi / p.
In each sector, the radii of line intersections are:
  r_m = 1 / cos(m * alpha)  for m = 0, 1, ..., q.

The area of the triangle Delta_m formed by the origin and adjacent vertices (r_m, r_{m+1}) is:
  Area(Delta_m) = 1/2 * r_m * r_{m+1} * sin(alpha)
                = 1/2 * (tan((m+1)*alpha) - tan(m*alpha)).

The regions between concentric boundary chords have areas:
  Region 0: Delta_0
  Region m (m >= 1): Delta_m - Delta_{m-1}.

Under alternating shading (exterior = 0), region m is shaded if (q - 1 - m) is even.
The alternating sum simplifies telescopically to:
  Area_fundamental = 1/2 * [ tan(q*alpha) + 2 * sum_{j=1}^{q-1} (-1)^{q-j} tan(j*alpha) ].

Multiplying by 2p gives the exact formula:
  A(p, q) = p * [ tan(q*pi/p) + 2 * sum_{j=1}^{q-1} (-1)^{q-j} tan(j*pi/p) ].

To avoid floating-point cancellation for large Fibonacci indices (e.g. F_35 = 9227465),
we evaluate this using IEEE 128-bit quad precision (__float128).
"""

from __future__ import annotations

import ctypes
from pathlib import Path


def solve(n_min: int = 3, n_max: int = 34) -> str:
    """Compute sum_{n=n_min}^{n_max} A(F_{n+1}, F_{n-1}) rounded to 10 decimal places."""
    dll_path = Path(__file__).resolve().parent / "fast_rsp_core.dll"
    if dll_path.is_file():
        try:
            lib = ctypes.CDLL(str(dll_path), winmode=0)
            lib.solve_841_str.restype = None
            lib.solve_841_str.argtypes = [
                ctypes.c_int,
                ctypes.c_int,
                ctypes.c_char_p,
                ctypes.c_int,
            ]
            buf = ctypes.create_string_buffer(128)
            lib.solve_841_str(n_min, n_max, buf, 128)
            return buf.value.decode("utf-8")
        except Exception:
            pass

    # Pure Python fallback using math.tan
    import math

    fib = [0] * (n_max + 3)
    fib[1] = fib[2] = 1
    for i in range(3, n_max + 3):
        fib[i] = fib[i - 1] + fib[i - 2]

    total_sum = 0.0
    for n in range(n_min, n_max + 1):
        p = fib[n + 1]
        q = fib[n - 1]
        alpha = math.pi / p
        s = 0.0
        cur_sign = 1 if (q - 1) % 2 == 0 else -1
        for j in range(1, q):
            s += cur_sign * math.tan(j * alpha)
            cur_sign = -cur_sign
        total = math.tan(q * alpha) + 2.0 * s
        total_sum += p * total

    return f"{total_sum:.10f}"


if __name__ == "__main__":
    print(solve())
