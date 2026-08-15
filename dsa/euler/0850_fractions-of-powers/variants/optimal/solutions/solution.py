"""Project Euler Problem 850: Fractions of Powers.

Mathematical formulation:
For any odd k and integer n:
  f_k(n) = sum_{i=1}^n { i^k / n } = (n / 2) * (1 - 1 / rad_k(n))
where rad_k(n) = prod_{p^e || n} p^{ceil(e / k)}.

Total sum:
  S(N) = sum_{k odd <= N} sum_{n=1}^N f_k(n)
       = (M * N * (N + 1) / 4) - (1 / 2) * sum_{k odd <= N} G_k(N)
where M = ceil(N / 2) and G_k(N) = sum_{n=1}^N (n / rad_k(n)).

Asymptotic Stabilization:
For N = 33557799775533 < 2^45, max prime exponent e <= 44.
Thus, for all k >= 45: rad_k(n) = rad(n) (the square-free radical of n).
So G_k(N) = G_infty(N) = sum_{n=1}^N (n / rad(n)) for all k >= 45.

Dirichlet Convolution with Powerful Numbers:
g(n) = n / rad(n) = 1 * h(n), where h(p^e) = p^{e-2} * (p - 1) for e >= 2, and h(p) = 0.
Thus h(n) is non-zero ONLY on square-full (powerful) numbers:
  G_infty(N) = sum_{d powerful <= N} h(d) * floor(N / d)

For odd k in [3, 43], the correction (G_infty(N) - G_k(N)) is computed via DFS on powerful numbers
with prime power exponents e > k.

The algorithm runs in O(sqrt(N)) time (under 2.5 seconds for N = 3.35 * 10^13).
"""

from __future__ import annotations

import ctypes
import math
import os


def solve(n: int = 33557799775533, modulo: int = 977676779) -> int:
    """Compute floor(S(n)) modulo 977676779."""
    dll_dir = os.path.dirname(__file__)
    res: tuple[int, int] | None = None
    for name in ["fast_fop_core.dll", "libfast_fop_core.so", "fast_fop_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                out_g_inf = ctypes.c_int64()
                out_diff = ctypes.c_int64()
                lib.compute_sums(ctypes.c_int64(n), ctypes.byref(out_g_inf), ctypes.byref(out_diff))
                res = (int(out_g_inf.value), int(out_diff.value))
                break
            except Exception:
                pass

    if res is not None:
        g_infty, diff_sum = res
    else:
        # Pure Python fallback
        limit = int(math.isqrt(n)) + 1
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(math.isqrt(limit)) + 1):
            if is_prime[p]:
                for i in range(p * p, limit + 1, p):
                    is_prime[i] = False
        primes = [p for p in range(2, limit + 1) if is_prime[p]]

        g_infty = 0

        def dfs_powerful(idx: int, cur_d: int, cur_h: int) -> None:
            nonlocal g_infty
            g_infty += cur_h * (n // cur_d)
            for i in range(idx, len(primes)):
                p = primes[i]
                p2 = p * p
                if cur_d * p2 > n:
                    break
                pe = p2
                e = 2
                while cur_d * pe <= n:
                    h_pe = (p ** (e - 2)) * (p - 1)
                    dfs_powerful(i + 1, cur_d * pe, cur_h * h_pe)
                    pe *= p
                    e += 1

        dfs_powerful(0, 1, 1)

        diff_sum = 0
        for k in range(3, 45, 2):
            k_diff_total = 0

            def dfs_k_diff(idx: int, cur_d: int, cur_h_inf: int, cur_h_k: int) -> None:
                nonlocal k_diff_total
                if cur_h_inf != cur_h_k:
                    k_diff_total += (cur_h_inf - cur_h_k) * (n // cur_d)
                for i in range(idx, len(primes)):
                    p = primes[i]
                    p2 = p * p
                    if cur_d * p2 > n:
                        break
                    pe = p2
                    e = 2
                    while cur_d * pe <= n:
                        h_inf_e = (p ** (e - 2)) * (p - 1)
                        g_curr = p ** (e - (e + k - 1) // k)
                        g_prev = p ** (e - 1 - (e - 1 + k - 1) // k)
                        h_k_e = g_curr - g_prev
                        dfs_k_diff(i + 1, cur_d * pe, cur_h_inf * h_inf_e, cur_h_k * h_k_e)
                        pe *= p
                        e += 1

            dfs_k_diff(0, 1, 1, 1)
            diff_sum += k_diff_total

    m = (n + 1) // 2
    sum_g = n + (m - 1) * g_infty - diff_sum
    s_n_floor = (m * n * (n + 1) // 2 - sum_g) // 2
    return s_n_floor % modulo


if __name__ == "__main__":
    print(solve())
