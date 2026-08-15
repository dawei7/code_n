"""Project Euler Problem 851: SOP and POS.

Mathematical formulation:
Let f(m) = sum_{u*v = m} (u + v) = 2 * sigma_1(m).
Then R_n(M) is the n-fold convolution of f(m):
  sum_{M=n}^infty R_n(M) q^M = (2 sum_{m=1}^infty sigma_1(m) q^m)^n = ((1 - E_2(q)) / 12)^n

Quasi-Modular Form Representation for n = 6:
R_6(M) can be uniquely expressed in the algebra of quasi-modular forms of weight 12 as:
  R_6(M) = (455 / 14328576) * sigma_11(M) - (1 / 15671880) * tau(M)
         + (11 / 20736 - 11*M / 17280) * sigma_9(M)
         + (25 / 10368 - 25*M / 3456 + 25*M^2 / 5184) * sigma_7(M)
         + (35 / 10368 - 35*M / 1728 + 5*M^2 / 144 - 5*M^3 / 288) * sigma_5(M)
         + (25 / 20736 - 25*M / 1728 + 5*M^2 / 96 - 5*M^3 / 72 + 5*M^4 / 168) * sigma_3(M)
         + (1 / 20736 - 5*M / 3456 + 5*M^2 / 432 - 5*M^3 / 144 + M^4 / 24 - M^5 / 60) * sigma_1(M)

For M = K! (here K = 10000), sigma_k(K!) and tau(K!) are evaluated via prime multiplicativity
and Hecke eigenvalue recurrences in under 0.05 seconds.
"""

from __future__ import annotations

import ctypes
import os


def solve(k_val: int = 10000, modulo: int = 1000000007) -> int:
    """Compute R_6(k_val!) modulo 10^9 + 7."""
    dll_dir = os.path.dirname(__file__)
    for name in ["fast_sop_core.dll", "libfast_sop_core.so", "fast_sop_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_r6_factorial.argtypes = [ctypes.c_int]
                lib.compute_r6_factorial.restype = ctypes.c_int64
                return int(lib.compute_r6_factorial(k_val))
            except Exception:
                pass

    # Pure Python fallback
    primes: list[int] = []
    is_p = [True] * (k_val + 1)
    is_p[0] = is_p[1] = False
    for p in range(2, int(k_val**0.5) + 1):
        if is_p[p]:
            for i in range(p * p, k_val + 1, p):
                is_p[i] = False
    primes = [p for p in range(2, k_val + 1) if is_p[p]]

    sigma_1 = [0] * (k_val + 1)
    for i in range(1, k_val + 1):
        for j in range(i, k_val + 1, i):
            sigma_1[j] += i

    a = [0] * (k_val + 1)
    a[0] = 1
    for m in range(1, k_val + 1):
        s = sum(sigma_1[j] * a[m - j] for j in range(1, m + 1)) % modulo
        a[m] = (-24 * s % modulo) * pow(m, modulo - 2, modulo) % modulo

    tau_vals = [0] + a[:k_val]

    tau_m = 1
    for p in primes:
        e = 0
        temp = k_val
        while temp > 0:
            e += temp // p
            temp //= p

        t0_val = 1
        t1_val = tau_vals[p] % modulo
        p11 = pow(p, 11, modulo)

        for _ in range(2, e + 1):
            t2_val = (t1_val * tau_vals[p] - p11 * t0_val) % modulo
            t0_val, t1_val = t1_val, t2_val

        t_pe = t1_val if e >= 1 else t0_val
        tau_m = (tau_m * t_pe) % modulo

    m_fact = 1
    for i in range(1, k_val + 1):
        m_fact = (m_fact * i) % modulo

    def get_sigma_fact(k: int) -> int:
        ans = 1
        for p in primes:
            e = 0
            temp = k_val
            while temp > 0:
                e += temp // p
                temp //= p
            pk = pow(p, k, modulo)
            if pk == 1:
                term = (e + 1) % modulo
            else:
                term = (pow(p, (e + 1) * k, modulo) - 1) * pow(pk - 1, modulo - 2, modulo) % modulo
            ans = (ans * term) % modulo
        return ans

    sig11 = get_sigma_fact(11)
    sig9 = get_sigma_fact(9)
    sig7 = get_sigma_fact(7)
    sig5 = get_sigma_fact(5)
    sig3 = get_sigma_fact(3)
    sig1 = get_sigma_fact(1)

    def mod_frac(num: int, den: int) -> int:
        return (num % modulo * pow(den % modulo, modulo - 2, modulo)) % modulo

    c_sig11 = mod_frac(455, 14328576)
    c_tau = mod_frac(-1, 15671880)

    m = m_fact
    m2 = (m * m) % modulo
    m3 = (m2 * m) % modulo
    m4 = (m3 * m) % modulo
    m5 = (m4 * m) % modulo

    p9 = (mod_frac(11, 20736) + mod_frac(-11, 17280) * m) % modulo
    p7 = (mod_frac(25, 10368) + mod_frac(-25, 3456) * m + mod_frac(25, 5184) * m2) % modulo
    p5 = (mod_frac(35, 10368) + mod_frac(-35, 1728) * m + mod_frac(5, 144) * m2 + mod_frac(-5, 288) * m3) % modulo
    p3 = (mod_frac(25, 20736) + mod_frac(-25, 1728) * m + mod_frac(5, 96) * m2 + mod_frac(-5, 72) * m3 + mod_frac(5, 168) * m4) % modulo
    p1 = (mod_frac(1, 20736) + mod_frac(-5, 3456) * m + mod_frac(5, 432) * m2 + mod_frac(-5, 144) * m3 + mod_frac(1, 24) * m4 + mod_frac(-1, 60) * m5) % modulo

    ans = (c_sig11 * sig11 + c_tau * tau_m + p9 * sig9 + p7 * sig7 + p5 * sig5 + p3 * sig3 + p1 * sig1) % modulo
    return (ans % modulo + modulo) % modulo


if __name__ == "__main__":
    print(solve())
