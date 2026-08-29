"""Project Euler 338: Cutting Rectangular Grid Paper

Find G(10^12) mod 10^8, where G(N) is the sum of F(w, h) for all 0 < h <= w <= N.
"""

from __future__ import annotations

import math


def solve(limit: int = 1_000_000_000_000, mod: int = 100_000_000) -> str:
    """Calculates G(limit) mod mod in pure Python using the algebraic identity

    G(N) = S1(N) - D_3(N) + D(N)
    where S1 is evaluated in O(sqrt(N)) via quotient grouping and D_3 via 3D Dirichlet hyperbola.
    """
    n = limit
    sqrt_n = math.isqrt(n)

    # 1. S1 in O(sqrt(N)) via quotient grouping
    s1 = 0
    for i in range(2, sqrt_n + 1):
        s1 = (s1 + (n // i) * (n // (i - 1))) % mod

    for q in range(1, n // (sqrt_n + 1) + 1):
        l_q = max(sqrt_n + 1, n // (q + 1) + 1)
        r_q = n // q
        if r_q >= l_q:
            term_boundary = q * (n // (l_q - 1))
            term_interior = (r_q - l_q) * (q * q)
            s1 = (s1 + term_boundary + term_interior) % mod

    # 2. D(N) in O(sqrt(N)) via 2D Dirichlet hyperbola
    def d_hyp(x: int) -> int:
        sx = math.isqrt(x)
        val = -sx * sx
        for a in range(1, sx + 1):
            val += 2 * (x // a)
        return val % mod

    d_n = d_hyp(n)

    # 3. D_3(N) in O(N^{2/3}) via 3D Dirichlet hyperbola
    k = int(n ** (1 / 3.0))
    while (k + 1) ** 3 <= n:
        k += 1
    while k**3 > n:
        k -= 1

    sum1 = 0
    for a in range(1, k + 1):
        sum1 = (sum1 + d_hyp(n // a)) % mod

    sum2 = 0
    for a in range(1, k + 1):
        na = n // a
        for b in range(1, k + 1):
            sum2 = (sum2 + na // b) % mod

    d3_n = (3 * sum1 - 3 * sum2 + pow(k, 3, mod)) % mod
    g_n = (s1 - d3_n + d_n) % mod
    return str(g_n)


if __name__ == "__main__":
    print(solve())
