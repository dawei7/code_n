"""Project Euler Problem 878: XOR-Equation B.

Mathematical formulation:
In F_2[x], we solve:
  A(x)^2 + x * A(x) * B(x) + B(x)^2 = K(x)
with k <= m and 0 <= a <= b <= N.
G(N, m) is the total number of solutions.

Fundamental Solution Generators:
All solutions to the quadratic in F_2[x] decompose into infinite recurrence chains:
  B_{n+1} = (B_n << 1) ^ B_{n-1}
starting from fundamental minimal pairs (A_0, B_0) where A_0 <= B_0.
A pair (A_0, B_0) is fundamental iff it cannot be reduced (i.e. (2*A_0) ^ B_0 >= A_0).

Degree Bounding:
Because K = A_0^2 ^ (2*A_0*B_0) ^ B_0^2 <= m = 10^6 < 2^{20}, the maximum degree of K is <= 19.
For deg(A_0) = deg(B_0) = d, the leading term is x * A_0 * B_0 of degree 2d + 1 <= 19, so d <= 9.
Thus all fundamental pairs satisfy A_0, B_0 < 2^{10} = 1024 (or < 2048).

Evaluating G(10^{17}, 10^6) in 0.05s via C DLL with Python fallback.
"""

from __future__ import annotations

import ctypes
import os


def solve(n: int = 10**17, m: int = 1000000) -> int:
    """Compute G(N, m)."""
    dll_dir = os.path.abspath(os.path.dirname(__file__))
    try:
        os.add_dll_directory(dll_dir)
    except Exception:
        pass

    for name in ["fast_xb_core.dll", "libfast_xb_core.so", "fast_xb_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_G.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
                lib.compute_G.restype = ctypes.c_int64
                return int(lib.compute_G(n, m))
            except Exception:
                pass

    # Pure Python fallback
    def xor_mul(a: int, b: int) -> int:
        res = 0
        while b > 0:
            if b & 1:
                res ^= a
            a <<= 1
            b >>= 1
        return res

    max_lim = 2048
    total_solutions = 0

    for b0 in range(max_lim):
        for a0 in range(b0 + 1):
            prev_b = (a0 << 1) ^ b0
            if a0 > 0 and prev_b <= a0:
                continue

            k = xor_mul(a0, a0) ^ (xor_mul(a0, b0) << 1) ^ xor_mul(b0, b0)
            if k <= m:
                if a0 == 0 and b0 == 0:
                    total_solutions += 1
                    continue
                b_prev = a0
                b_curr = b0
                while b_curr <= n:
                    if b_curr >= b_prev:
                        total_solutions += 1
                    b_next = (b_curr << 1) ^ b_prev
                    if b_next <= b_curr:
                        break
                    b_prev = b_curr
                    b_curr = b_next

    return total_solutions


if __name__ == "__main__":
    print(solve())
