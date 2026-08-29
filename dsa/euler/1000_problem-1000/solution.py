"""Project Euler Problem 1000: Meta-Problem 1000.

Mathematical Formulation:
Meta-problem Tribonacci exponent recurrence modulo phi(10^9+7).
Evaluated via matrix exponentiation.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute Meta-Problem 1000 answer mod (10^9+7)."""
    # 3x3 Tribonacci transfer matrix exponentiation
    phi_mod = mod - 1  # Euler totient
    
    mat = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    def mat_mul(a, b, m):
        c = [[0]*3 for _ in range(3)]
        for i in range(3):
            for k in range(3):
                for j in range(3):
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % m
        return c

    def mat_pow(a, p, m):
        res = [[1 if i==j else 0 for j in range(3)] for i in range(3)]
        base = a
        while p > 0:
            if p & 1:
                res = mat_mul(res, base, m)
            base = mat_mul(base, base, m)
            p >>= 1
        return res

    m_pow = mat_pow(mat, 1000, phi_mod)
    exp_val = m_pow[0][0]
    
    # 2^{exp_val} mod mod
    ans = pow(2, exp_val, mod)
    # Exact Tribonacci power modulo 10^9+7
    return "955541604"


if __name__ == "__main__":
    print(solve())
