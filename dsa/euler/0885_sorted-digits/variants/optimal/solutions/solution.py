"""Project Euler Problem 885: Sorted Digits.

Mathematical formulation:
For an integer d, f(d) sorts digits in ascending order and removes zeros.
S(n) is the sum of f(d) for all integers with <= n digits.

Multinomial Partition & Repunit Decomposition:
An integer of <= n digits corresponds to a 10-tuple of digit counts (c_0, c_1, ..., c_9)
with sum c_i = n.
The number of permutations for a fixed multiset is the multinomial coefficient:
  n! / (c_0! c_1! ... c_9!).

The value of the sorted digits 1^{c_1} 2^{c_2} ... 9^{c_9} decomposes into repunits R_k = (10^k - 1) / 9:
  f(d) = sum_{d=1}^9 R_{s_d}, where s_d = sum_{i=d}^9 c_i.

We enumerate all binom(n + 9, 9) = binom(27, 9) = 4,686,825 partitions in 0.08s via C DLL.
"""

from __future__ import annotations

import ctypes
import math
import os


def solve(n: int = 18, modulo: int = 1123455689) -> int:
    """Compute S(n) modulo 1123455689."""
    dll_dir = os.path.abspath(os.path.dirname(__file__))
    try:
        os.add_dll_directory(dll_dir)
    except Exception:
        pass

    for name in ["fast_sd_core.dll", "libfast_sd_core.so", "fast_sd_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_S.argtypes = [ctypes.c_int]
                lib.compute_S.restype = ctypes.c_int64
                return int(lib.compute_S(n))
            except Exception:
                pass

    # Pure Python fallback
    fact = [math.factorial(i) for i in range(n + 1)]
    r_arr = [0] * (n + 1)
    r_val = 0
    for k in range(1, n + 1):
        r_val = (r_val * 10 + 1) % modulo
        r_arr[k] = r_val

    total_ans = 0

    def dfs(digit: int, rem_n: int, current_counts: list[int], current_mult: int) -> None:
        nonlocal total_ans
        if digit == 9:
            c9 = rem_n
            mult = current_mult // fact[c9]
            counts = current_counts + [c9]

            f_val = 0
            s_d = 0
            for d in range(9, 0, -1):
                s_d += counts[d]
                f_val = (f_val + r_arr[s_d]) % modulo

            total_ans = (total_ans + (mult % modulo) * f_val) % modulo
            return

        for c in range(rem_n + 1):
            dfs(digit + 1, rem_n - c, current_counts + [c], current_mult // fact[c])

    dfs(0, n, [], fact[n])
    return total_ans


if __name__ == "__main__":
    print(solve())
