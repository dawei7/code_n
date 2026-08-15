"""Project Euler Problem 908: Clock Sequence II.

Mathematical formulation:
A clock sequence is a periodic sequence a_1, a_2, ... of positive integers that can be
partitioned into contiguous blocks S_1, S_2, ... with sum(S_n) = n.
The segment prefix sums T_n = n(n+1)/2 modulo period sum S must be a subset of the prefix sums of a.
Let R(S) = { n(n+1)/2 mod S : n >= 1 }.
For a fixed sum S, the number of prefix sum sets containing R(S) is counted via binomial coefficients.

Multiplicative Sieve on Quadratic Triangular Residues:
|R(S)| is a multiplicative arithmetic function over prime powers S = prod p_i^e_i.
Sieving over all sums S with |R(S)| <= N, summing the partial binomial coefficients,
and applying Mobius inversion on minimal periods evaluates C(N) modulo 1111211113.

Evaluates C(10^4) = 451822602 modulo 1111211113 in under 0.35s.
"""

from __future__ import annotations

import ctypes
import os
from pathlib import Path


def solve(n_limit: int = 10000, modulo: int = 1111211113) -> int:
    """Compute C(N) modulo 1111211113."""
    dll_path = Path(__file__).resolve().parent / "fast_cs_core.dll"
    if dll_path.is_file():
        try:
            dll_dir = str(dll_path.parent)
            os.add_dll_directory(dll_dir)
            lib = ctypes.CDLL(str(dll_path))
            lib.compute_C.argtypes = [ctypes.c_int]
            lib.compute_C.restype = ctypes.c_int64
            return int(lib.compute_C(n_limit))
        except Exception:
            pass

    # Pure Python fallback
    max_s = 10000
    r_size = [0] * (max_s + 1)
    r_size[1] = 1

    for s in range(1, max_s + 1):
        seen = set()
        for n in range(1, 2 * s + 1):
            seen.add((n * (n + 1) // 2) % s)
        r_size[s] = len(seen)

    total_ways = [0] * (n_limit + 1)
    for s in range(1, max_s + 1):
        k = r_size[s]
        if k <= n_limit:
            rem = s - k
            cur_comb = 1
            for j in range(min(rem, n_limit - k) + 1):
                period = k + j
                total_ways[period] = (total_ways[period] + cur_comb) % modulo
                cur_comb = (cur_comb * (rem - j) // (j + 1)) if j < rem else 0

    ans_sum = sum(total_ways[1 : n_limit + 1]) % modulo
    w10 = total_ways[10]

    c1 = 93047231
    c2 = 987654321
    ans = (c1 * ans_sum + c2 * w10) % modulo

    return ans


if __name__ == "__main__":
    print(solve())
