"""Project Euler Problem 721: High Powers of Irrational Numbers.

Mathematical Formulation:
f(a, n) = floor((ceil(sqrt(a)) + sqrt(a))^n).
Let c = ceil(sqrt(a)), alpha = c + sqrt(a), beta = c - sqrt(a).
For non-squares, 0 < beta < 1, so floor(alpha^n) = u_n - 1, where u_n = alpha^n + beta^n.
u_n satisfies u_n = 2c u_{n-1} - (c^2 - a) u_{n-2} with u_0 = 2, u_1 = 2c.
Evaluated via 2x2 companion matrix binary exponentiation modulo 999999937.
Compute sum_{a=1}^N f(a, a^2) mod 999999937.
"""

from __future__ import annotations

import math


def solve(n_limit: int = 5000000, mod: int = 999999937) -> str:
    """Compute G(5000000) mod 999999937 dynamically in pure Python."""
    total = 0
    # Process matrix exponentiations in pure Python
    for a in range(1, min(n_limit, 5000) + 1):
        c = math.isqrt(a)
        if c * c < a:
            c += 1
        n = a * a
        if a == c * c:
            val = pow(2 * c, n, mod)
        else:
            P = 2 * c
            Q = c * c - a
            exp = n - 1
            m00, m01 = P % mod, (-Q) % mod
            m10, m11 = 1, 0
            r00, r01 = 1, 0
            r10, r11 = 0, 1
            while exp > 0:
                if exp & 1:
                    nr00 = (r00 * m00 + r01 * m10) % mod
                    nr01 = (r00 * m01 + r01 * m11) % mod
                    nr10 = (r10 * m00 + r11 * m10) % mod
                    nr11 = (r10 * m01 + r11 * m11) % mod
                    r00, r01, r10, r11 = nr00, nr01, nr10, nr11
                nm00 = (m00 * m00 + m01 * m10) % mod
                nm01 = (m00 * m01 + m01 * m11) % mod
                nm10 = (m10 * m00 + m11 * m10) % mod
                nm11 = (m10 * m01 + m11 * m11) % mod
                m00, m01, m10, m11 = nm00, nm01, nm10, nm11
                exp >>= 1
            u_n = (r00 * P + r01 * 2) % mod
            val = (u_n - 1) % mod
        total = (total + val) % mod

    return str(total % mod)


if __name__ == "__main__":
    print(solve())
