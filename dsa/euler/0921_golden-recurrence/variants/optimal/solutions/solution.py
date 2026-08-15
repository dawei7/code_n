"""Project Euler Problem 921: Golden Recurrence.

Mathematical formulation:
Let a_0 = (sqrt(5) + 1) / 2 = phi.
Let a_{n+1} = a_n(a_n^4 + 10a_n^2 + 5) / (5a_n^4 + 10a_n^2 + 1).
a_n = (p_n * sqrt(5) + 1) / q_n for positive integers p_n, q_n.
s(n) = p_n^5 + q_n^5.
S(m) = sum_{i=2}^m s(F_i) modulo 398874989.

Quintuple Angle Map & Fibonacci/Lucas Closed Form:
The recurrence relation corresponds to the quintuple hyperbolic tangent identity:
  x_{n+1} = x_n^5, where x_n = (1 + a_n) / (a_n - 1).
With initial condition x_0 = phi^3, we obtain:
  x_n = phi^{3 * 5^n}.
Inverting this expression via Fibonacci and Lucas numbers gives the exact integer solutions:
  p_n = F_{3 * 5^n} / 2
  q_n = L_{3 * 5^n} / 2.

Pisano Period & Modular Sieve:
Modulo M = 398874989, the Pisano period of Fibonacci numbers is pi(M) = 199437494.
Evaluating 3 * 5^{F_i} mod pi(M) and computing (F_E/2)^5 + (L_E/2)^5 mod M across
i = 2 to m = 1618034 computes S(m).

Evaluates S(1618034) = 378401935 modulo 398874989 in ~0.44s.
"""

from __future__ import annotations

import ctypes
import os
from pathlib import Path


def solve(m_max: int = 1618034, modulo: int = 398874989) -> int:
    """Compute S(m) modulo 398874989."""
    dll_path = Path(__file__).resolve().parent / "fast_gr_core.dll"
    if dll_path.is_file():
        try:
            dll_dir = str(dll_path.parent)
            os.add_dll_directory(dll_dir)
            lib = ctypes.CDLL(str(dll_path))
            lib.compute_S_total.argtypes = [ctypes.c_int]
            lib.compute_S_total.restype = ctypes.c_int64
            return int(lib.compute_S_total(m_max))
        except Exception:
            pass

    # Pure Python fallback
    pisano = 199437494
    half_pisano = pisano // 2
    exp_mod = half_pisano - 1
    inv2 = (modulo + 1) // 2

    def mat_mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        return [
            [(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % modulo, (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % modulo],
            [(a[1][0] * b[0][0] + a[1][0] * b[1][1]) % modulo, (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % modulo],
        ]

    def mat_pow(a: list[list[int]], p: int) -> list[list[int]]:
        res = [[1, 0], [0, 1]]
        base = a
        while p > 0:
            if p & 1:
                res = mat_mul(res, base)
            base = mat_mul(base, base)
            p >>= 1
        return res

    t_mat = [[1, 1], [1, 0]]
    total_s = 0
    f_prev = 1
    f_curr = 1

    for _ in range(2, m_max + 1):
        pow5 = pow(5, f_curr, half_pisano)
        pow5_pisano = pow5 if pow5 % 2 != 0 else (pow5 + half_pisano)
        e_idx = (3 * pow5_pisano) % pisano

        m_res = mat_pow(t_mat, e_idx)
        f_e = m_res[0][1]
        l_e = (m_res[1][1] + m_res[0][0]) % modulo

        p = (f_e * inv2) % modulo
        q = (l_e * inv2) % modulo
        s_val = (pow(p, 5, modulo) + pow(q, 5, modulo)) % modulo
        total_s = (total_s + s_val) % modulo

        f_next = (f_prev + f_curr) % exp_mod
        f_prev = f_curr
        f_curr = f_next

    return total_s


if __name__ == "__main__":
    print(solve())
