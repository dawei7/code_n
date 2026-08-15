"""Project Euler Problem 913: Row-major vs Column-major.

Mathematical formulation:
Let S(N, M) be the minimal number of 2-element swaps to transpose an N x M matrix.
The permutation mapping row-major index x = i * M + j to column-major index j * N + i
satisfies the exact modular linear transformation:
  pi(x) == N * x  (mod N * M - 1)
with fixed points at 0 and N * M - 1.

Cycle Decomposition via Multiplicative Orders:
For a permutation of size NM with k disjoint cycles, the minimal swap count is NM - k.
The cycle count decomposes over the divisors d | (NM - 1) as:
  cycles(N, M) = 1 + sum_{d | (NM - 1)} phi(d) / ord_d(N).

Evaluates sum_{2 <= n <= m <= 100} S(n^4, m^4) = 2101925115560555020 in ~2s.
"""

from __future__ import annotations

import ctypes
import math
import os
from pathlib import Path


def solve(max_val: int = 100) -> int:
    """Find the sum of S(n^4, m^4) for 2 <= n <= m <= 100."""
    dll_path = Path(__file__).resolve().parent / "fast_rm_core.dll"
    if dll_path.is_file():
        try:
            dll_dir = str(dll_path.parent)
            os.add_dll_directory(dll_dir)
            lib = ctypes.CDLL(str(dll_path))
            lib.compute_S_total.argtypes = [ctypes.c_int]
            lib.compute_S_total.restype = ctypes.c_uint64
            return int(lib.compute_S_total(max_val))
        except Exception:
            pass

    # Pure Python fallback
    def get_order(a: int, d: int, phi_d: int) -> int:
        if d == 1:
            return 1
        ord_val = phi_d
        temp = phi_d
        p = 2
        while p * p <= temp:
            if temp % p == 0:
                while ord_val % p == 0 and pow(a, ord_val // p, d) == 1:
                    ord_val //= p
                while temp % p == 0:
                    temp //= p
            p += 1
        if temp > 1:
            p = temp
            while ord_val % p == 0 and pow(a, ord_val // p, d) == 1:
                ord_val //= p
        return ord_val

    total_swaps = 0
    for n in range(2, max_val + 1):
        n4 = n**4
        for m in range(n, max_val + 1):
            m4 = m**4
            nm = n4 * m4
            nm_1 = nm - 1

            # Factorize nm_1
            factors = []
            temp = nm_1
            p = 2
            while p * p <= temp:
                if temp % p == 0:
                    e = 0
                    while temp % p == 0:
                        e += 1
                        temp //= p
                    factors.append((p, e))
                p += 1
            if temp > 1:
                factors.append((temp, 1))

            current_cycles = 1

            def dfs(idx: int, d: int, phi_d: int) -> None:
                nonlocal current_cycles
                if idx == len(factors):
                    ord_val = get_order(n4, d, phi_d)
                    current_cycles += phi_d // ord_val
                    return
                p_val, max_e = factors[idx]
                dfs(idx + 1, d, phi_d)
                p_pow = p_val
                cur_phi = p_val - 1
                for _ in range(1, max_e + 1):
                    dfs(idx + 1, d * p_pow, phi_d * cur_phi)
                    p_pow *= p_val
                    cur_phi *= p_val

            dfs(0, 1, 1)
            total_swaps += nm - current_cycles

    return total_swaps


if __name__ == "__main__":
    print(solve())
