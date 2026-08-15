"""Project Euler Problem 840: Sum of Products.

Mathematical reduction:
D(n) is the arithmetic derivative defined by:
  D(1) = 1, D(p) = 1 for prime p, and D(pq) = D(p)q + p D(q).
For a partition lambda = {a_1, a_2, ..., a_k} of n, its weight is P = prod D(a_j).
G(n) is the sum of P over all partitions of n.

The generating function F(x) = sum_{n=0}^infty G(n) x^n is:
  F(x) = prod_{k=1}^infty 1 / (1 - D(k) x^k)

Taking the logarithmic derivative:
  A(x) = x * F'(x) / F(x) = x * d/dx ln F(x)
       = sum_{k=1}^infty sum_{j=1}^infty k * D(k)^j * x^{k j}
Let A(x) = sum_{m=1}^infty c_m x^m, where:
  c_m = sum_{k | m} k * D(k)^{m/k}

Then x F'(x) = A(x) F(x) yields the Euler partition-style linear recurrence:
  n * G(n) = sum_{m=1}^n c_m * G(n - m)
  G(n) = 1/n * sum_{m=1}^n c_m * G(n - m)

We compute c_m in O(N log N) time, and G(n) for n = 1..N in O(N^2) time modulo 999676999.
"""

from __future__ import annotations

import ctypes
from pathlib import Path


def solve(n: int = 50000, mod: int = 999676999) -> int:
    """Compute S(N) = sum_{n=1}^N G(n) modulo mod."""
    dll_path = Path(__file__).resolve().parent / "fast_sop_core.dll"
    if dll_path.is_file():
        try:
            lib = ctypes.CDLL(str(dll_path), winmode=0)
            lib.compute_S.restype = ctypes.c_int64
            lib.compute_S.argtypes = [ctypes.c_int32, ctypes.c_int64]
            return int(lib.compute_S(n, mod))
        except Exception:
            pass

    # Pure Python fallback
    d_val = [0] * (n + 1)
    d_val[1] = 1
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i

    for i in range(2, n + 1):
        p = spf[i]
        rem = i // p
        if rem == 1:
            d_val[i] = 1
        else:
            d_val[i] = (d_val[p] * rem + p * d_val[rem]) % mod

    c = [0] * (n + 1)
    for k in range(1, n + 1):
        d_k = d_val[k] % mod
        pow_d = d_k
        m = k
        while m <= n:
            c[m] = (c[m] + k * pow_d) % mod
            pow_d = (pow_d * d_k) % mod
            m += k

    g = [0] * (n + 1)
    g[0] = 1

    inv = [0] * (n + 1)
    inv[1] = 1
    for i in range(2, n + 1):
        inv[i] = (mod - mod // i) * inv[mod % i] % mod

    for curr_n in range(1, n + 1):
        s = 0
        for m in range(1, curr_n + 1):
            s = (s + c[m] * g[curr_n - m]) % mod
        g[curr_n] = (s * inv[curr_n]) % mod

    return sum(g[1 : n + 1]) % mod


if __name__ == "__main__":
    print(solve())
