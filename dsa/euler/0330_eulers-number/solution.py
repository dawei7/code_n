"""Project Euler 330: Euler's Number

Find (A(10^9) + B(10^9)) mod 77777777, where a(n) = (A(n)*e + B(n)) / n!
satisfies the infinite summation recurrence a(n) = sum_{i=1}^infty a(n - i) / i!.
"""

from __future__ import annotations

import math

PRIMES: list[int] = [7, 11, 73, 101, 137]
MOD_TARGET: int = 77_777_777


def solve(n: int = 1_000_000_000, mod: int = MOD_TARGET) -> str:
    """Calculates (A(n) + B(n)) mod mod using the Fubini/ordered Bell generating function

    C(n) = - sum_{k=1}^n (n! / k!) * F_k, prime truncation modulo p, and Chinese Remainder Theorem.
    """
    rem_list: list[int] = []

    for p in PRIMES:
        # Precompute basis coefficients c_j for Fubini numbers modulo p:
        # F_n = sum_{j=1}^{p-1} c_j * j^n mod p
        c = [0] * p
        for j in range(1, p):
            s = 0
            for m in range(j, p):
                sign = 1 if (m - j) % 2 == 0 else -1
                s = (s + sign * math.comb(m, j)) % p
            c[j] = s % p

        def get_fubini(k_val: int) -> int:
            exp = k_val % (p - 1)
            if exp == 0 and k_val > 0:
                exp = p - 1
            return sum(c[j] * pow(j, exp, p) for j in range(1, p)) % p

        # Modulo p: (n! / (n - d)!) is non-zero only for d in 0 .. p - 2
        tot_p = 0
        fall = 1
        for d in range(p - 1):
            k = n - d
            if d > 0:
                fall = (fall * (n - d + 1)) % p
            fk = get_fubini(k)
            tot_p = (tot_p + fall * fk) % p

        tot_p = (-tot_p) % p
        rem_list.append(tot_p)

    # Reconstruct modulo mod = 77777777 via Chinese Remainder Theorem
    ans = 0
    for r, p in zip(rem_list, PRIMES):
        m_i = mod // p
        inv = pow(m_i, -1, p)
        ans = (ans + r * m_i * inv) % mod

    return str(ans)


if __name__ == "__main__":
    print(solve())
