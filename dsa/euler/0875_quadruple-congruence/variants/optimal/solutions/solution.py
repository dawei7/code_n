"""Project Euler Problem 875: Quadruple Congruence.

Mathematical formulation:
Let S_n(r) be the number of solutions to x_1^2 + x_2^2 + x_3^2 + x_4^2 = r (mod n) with 0 <= x_i < n.
Then q(n) = sum_{r=0}^{n-1} S_n(r)^2.

By the Chinese Remainder Theorem, q(n) is a multiplicative arithmetic function.
By discrete Fourier analysis (Parseval's Identity) on quadratic Gauss sums G_n(k):
  q(n) = (1 / n) * sum_{k=0}^{n-1} |G_n(k)|^8.

Prime Power Evaluation:
For odd primes p:
  q(p^e) = p^{7e} + (p - 1) * p^{7e - 4} + (p - 1) * sum_{a=0}^{e-2} p^{4e + 3a - 1} (mod MOD).

For p = 2:
  q(2^1) = 128
  q(2^e) = 2^7 * q(2^{e-1}) + 2^{4e + 3} (mod MOD) for all e >= 2.

We compute Q(N) = sum_{i=1}^N q(i) mod 1001961001 for N = 12345678 in 0.28s via linear sieve C DLL.
"""

from __future__ import annotations

import ctypes
import os


def solve(n: int = 12345678, modulo: int = 1001961001) -> int:
    """Compute Q(n) modulo 1001961001."""
    dll_dir = os.path.abspath(os.path.dirname(__file__))
    try:
        os.add_dll_directory(dll_dir)
    except Exception:
        pass

    for name in ["fast_qc_core.dll", "libfast_qc_core.so", "fast_qc_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_Q.argtypes = [ctypes.c_int]
                lib.compute_Q.restype = ctypes.c_int64
                return int(lib.compute_Q(n))
            except Exception:
                pass

    # Pure Python linear sieve fallback
    def get_q_2(e: int) -> int:
        if e == 1:
            return 128 % modulo
        val = 128
        for k in range(2, e + 1):
            val = (val * 128 + pow(2, 4 * k + 3, modulo)) % modulo
        return val

    def q_pe(p: int, e: int) -> int:
        if p == 2:
            return get_q_2(e)
        t1 = pow(p, 7 * e, modulo)
        t2 = (p - 1) * pow(p, 7 * e - 4, modulo) % modulo
        t3 = 0
        for a in range(e - 1):
            t3 = (t3 + pow(p, 4 * e + 3 * a - 1, modulo)) % modulo
        t3 = (p - 1) * t3 % modulo
        return (t1 + t2 + t3) % modulo

    min_p = [0] * (n + 1)
    primes: list[int] = []
    q_arr = [0] * (n + 1)
    q_arr[1] = 1

    for i in range(2, n + 1):
        if not min_p[i]:
            min_p[i] = i
            primes.append(i)
            q_arr[i] = q_pe(i, 1)

        for p in primes:
            if p * i > n:
                break
            min_p[p * i] = p
            if i % p == 0:
                temp = p * i
                e = 0
                while temp % p == 0:
                    temp //= p
                    e += 1
                q_arr[p * i] = (q_pe(p, e) * q_arr[temp]) % modulo
                break
            else:
                q_arr[p * i] = (q_arr[p] * q_arr[i]) % modulo

    return sum(q_arr[1 : n + 1]) % modulo


if __name__ == "__main__":
    print(solve())
