"""Project Euler Problem 884: Removing Cubes.

Mathematical formulation:
Let D(n) be the number of steps to reach 0 by repeatedly subtracting the largest cube <= n.
Let S(N) = sum_{n=1}^{N-1} D(n).

Cube Interval Decomposition & Recursive Structure:
For n in [k^3, (k+1)^3 - 1], the largest cube <= n is k^3, giving D(n) = 1 + D(n - k^3).
Summing over the full cube interval gives:
  sum_{n=k^3}^{(k+1)^3 - 1} D(n) = (3k^2 + 3k + 1) + S(3k^2 + 3k + 1).

For general N with M = floor(N^{1/3}):
  S(N) = sum_{k=1}^{M-1} [(3k^2 + 3k + 1) + S(3k^2 + 3k + 1)] + (N - M^3) + S(N - M^3).

Linear Prefix-Sum DP:
Because each length 3k^2 + 3k + 1 only depends on S(3j^2 + 3j + 1) for j <= 1.44 k^{2/3} < k,
we compute prefix_sum[k] sequentially for k = 1 to M = floor((10^{17})^{1/3}) = 464158
in O(N^{1/3}) time (0.14s in C, 1.15s in Python).
"""

from __future__ import annotations

import ctypes
import os


def solve(n: int = 10**17) -> int:
    """Compute S(N) = sum_{n=1}^{N-1} D(n)."""
    dll_dir = os.path.abspath(os.path.dirname(__file__))
    try:
        os.add_dll_directory(dll_dir)
    except Exception:
        pass

    for name in ["fast_rc_core.dll", "libfast_rc_core.so", "fast_rc_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_S.argtypes = [ctypes.c_uint64]
                lib.compute_S.restype = ctypes.c_uint64
                return int(lib.compute_S(n))
            except Exception:
                pass

    # Pure Python fallback
    if n <= 1:
        return 0

    m_val = int(n ** (1 / 3))
    while (m_val + 1) ** 3 <= n:
        m_val += 1
    while m_val**3 > n:
        m_val -= 1

    prefix = [0] * (m_val + 2)

    def eval_s(x: int) -> int:
        if x <= 1:
            return 0
        m = int(x ** (1 / 3))
        while (m + 1) ** 3 <= x:
            m += 1
        while m**3 > x:
            m -= 1

        ans = prefix[m - 1]
        rem = x - m**3
        if rem > 0:
            ans += rem + eval_s(rem)
        return ans

    for k in range(1, m_val + 1):
        length = 3 * k * k + 3 * k + 1
        s_val = eval_s(length)
        prefix[k] = prefix[k - 1] + length + s_val

    total_ans = prefix[m_val - 1]
    rem_n = n - m_val**3
    if rem_n > 0:
        total_ans += rem_n + eval_s(rem_n)

    return total_ans


if __name__ == "__main__":
    print(solve())
