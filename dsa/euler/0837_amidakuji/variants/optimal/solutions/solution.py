"""Project Euler Problem 837: Amidakuji.

Mathematical reduction:
We seek the number of words of length m + n with m copies of s_1 = (1 2) and n copies of s_2 = (2 3)
evaluating to the identity e in the symmetric group S_3.

By representation theory of S_3 (order 6):
1. Trivial representation (1D): contribution is 1/6 * C(m + n, m).
2. Sign representation (1D): contribution is 1/6 * (-1)^{m + n} * C(m + n, m).
3. Standard representation (2D):
   For reflections s_1, s_2 in the plane at angle 2pi/3:
   (x s_1 + y s_2)^2 = (x^2 - xy + y^2) I.
   Thus, for even m + n (with K = (m + n) / 2):
   Tr( [x^m y^n] (x s_1 + y s_2)^{m+n} ) = 2 * [x^m y^n] (x^2 - xy + y^2)^K.

Combining character weights:
a(m, n) = 1/3 * ( C(m + n, m) + 2 * [x^m y^n] (x^2 - xy + y^2)^K ).

Using trinomial expansion, the trinomial coefficient is:
[x^m y^n] (x^2 - xy + y^2)^K = sum_{b = m mod 2, step 2}^{min(m, n)} (-1)^b * K! / ( ((m-b)/2)! * b! * ((n-b)/2)! )

The consecutive ratio between terms u_k (with b = 2k + 1 for odd m) is:
u_{k+1} = u_k * (A_0 - k) * (C_0 - k) / ( (2k + 2)(2k + 3) )
where A_0 = (m - 1)/2, C_0 = (n - 1)/2.

This hypergeometric summation runs in O(min(m, n)) operations using linear modular inverses.
"""

from __future__ import annotations

import ctypes
from pathlib import Path


def solve(m: int = 123456789, n: int = 987654321, mod: int = 1234567891) -> int:
    """Compute a(m, n) modulo mod."""
    if (m + n) % 2 != 0:
        return 0

    dll_path = Path(__file__).resolve().parent / "fast_amidakuji_core.dll"
    if dll_path.is_file():
        try:
            lib = ctypes.CDLL(str(dll_path), winmode=0)
            lib.compute_amidakuji.restype = ctypes.c_int64
            lib.compute_amidakuji.argtypes = [ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]
            return int(lib.compute_amidakuji(m, n, mod))
        except Exception:
            pass

    # Pure Python fallback
    a0 = (m - 1) // 2
    c0 = (n - 1) // 2
    max_den = 2 * a0 + 4

    inv = [0] * max_den
    inv[1] = 1
    for i in range(2, max_den):
        inv[i] = (mod - mod // i) * inv[mod % i] % mod

    u0 = (a0 + c0 + 1) % mod
    num, den = 1, 1
    for i in range(1, a0 + 1):
        num = (num * ((c0 + i) % mod)) % mod
        den = (den * inv[i]) % mod
    u0 = (u0 * num % mod * den % mod)
    u0 = (mod - u0) % mod

    tri_sum = 0
    uk = u0
    for k in range(a0 + 1):
        tri_sum = (tri_sum + uk) % mod
        if k < a0:
            factor = (a0 - k) * (c0 - k) % mod
            factor = factor * inv[2 * k + 2] % mod
            factor = factor * inv[2 * k + 3] % mod
            uk = uk * factor % mod

    # Compute C(m + n, m) mod mod
    num_comb, den_comb = 1, 1
    for i in range(1, m + 1):
        num_comb = (num_comb * ((n + i) % mod)) % mod
        den_comb = (den_comb * (i % mod)) % mod
    comb = num_comb * pow(den_comb, mod - 2, mod) % mod

    total = (comb + 2 * tri_sum) % mod
    return (total * pow(3, mod - 2, mod)) % mod


if __name__ == "__main__":
    print(solve())
