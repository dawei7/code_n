"""Project Euler Problem 944: Sum of Elevisors.

Mathematical formulation:
For a subset E of {1, ..., n}, an element x in E is an elevisor of E if x divides another
element y in E with y != x.
sev(E) is the sum of elevisors of E.
S(n) is the sum of sev(E) over all 2^n subsets E.
Given:
  S(10) = 4927

Linearity of Expectation & Indicator Multiplicity:
For each element x in {1, ..., floor(n/2)}, the number of multiples strictly greater than x
is k - 1 where k = floor(n / x).
The number of subsets E containing x and at least one strictly greater multiple is:
  count(x) = 2^{n - 1} - 2^{n - k}.
Summing over all x <= floor(n/2) yields:
  S(n) = 2^{n - 1} * sum_{x=1}^{n/2} x - sum_{x=1}^{n/2} x * 2^{n - floor(n/x)}.

Hyperbolic Block Summation (Floor Division Sieve):
Grouping x by the quotient value k = floor(n / x) evaluates the sum in O(sqrt(n)) blocks.
For n = 10^{14}, stepping O(sqrt(n)) = 10^7 intervals modulo 1234567891 computes S(10^{14}).

Evaluates S(10^{14}) = 1228599511 modulo 1234567891 in ~10.7s (or C DLL).
"""

from __future__ import annotations

import ctypes
import os
from pathlib import Path


def solve(n: int = 10**14, modulo: int = 1234567891) -> int:
    """Compute S(n) modulo 1234567891."""
    dll_path = Path(__file__).resolve().parent / "fast_se_core.dll"
    if dll_path.is_file():
        try:
            dll_dir = str(dll_path.parent)
            os.add_dll_directory(dll_dir)
            lib = ctypes.CDLL(str(dll_path))
            lib.compute_S.argtypes = [ctypes.c_int64, ctypes.c_int64]
            lib.compute_S.restype = ctypes.c_int64
            return int(lib.compute_S(n, modulo))
        except Exception:
            pass

    # Pure Python fallback
    m = n // 2
    inv2 = (modulo + 1) // 2

    # Term 1: 2^{n - 1} * m(m + 1)/2
    sum_all_x = (m % modulo) * ((m + 1) % modulo) % modulo * inv2 % modulo
    term1 = (pow(2, n - 1, modulo) * sum_all_x) % modulo

    # Term 2: sum over hyperbolic blocks
    term2 = 0
    cur_x = 1
    while cur_x <= m:
        k = n // cur_x
        next_x = min(m, n // k)

        count = (next_x - cur_x + 1) % modulo
        sum_ends = (cur_x + next_x) % modulo
        sum_x_range = (count * sum_ends % modulo) * inv2 % modulo

        pow2 = pow(2, n - k, modulo)
        term2 = (term2 + sum_x_range * pow2) % modulo

        cur_x = next_x + 1

    return (term1 - term2 + modulo) % modulo


if __name__ == "__main__":
    print(solve())
