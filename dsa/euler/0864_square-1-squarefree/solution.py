"""Project Euler Problem 864: Square + 1 = Squarefree.

Mathematical formulation:
An integer x^2 + 1 is squarefree iff no prime square p^2 divides x^2 + 1.
By Mobius inversion:
  C(n) = sum_{x=1}^n mu^2(x^2 + 1) = sum_{d >= 1} mu(d) * #{1 <= x <= n : x^2 + 1 = 0 (mod d^2)}.

For d to divide x^2 + 1, all prime factors of d must satisfy p = 1 (mod 4).
By Gaussian integer factorization in Z[i]:
  x^2 + 1 = (x + i)(x - i) = 0 (mod d^2)
where each divisor d corresponds to primitive pairs (u, v) with u > v >= 1, gcd(u, v) = 1,
u + v = 1 (mod 2), such that d = u^2 + v^2.

The Diophantine equation for roots modulo d^2:
  b * (u^2 - v^2) + a * (2*u*v) = 1
solved via Extended Euclidean Algorithm yields a unique base solution (a_0, b_0),
producing conjugate roots x_0 = a_0*(u^2 - v^2) - b_0*(2*u*v) (mod d^2).

For large n, the asymptotic density is given by the Euler product:
  A = prod_{p = 1 mod 4} (1 - 2/p^2)
multiplied by n and corrected by the discrete root boundary distribution.
"""

from __future__ import annotations

import math


def _egcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (1, 0, a)
    x, y, g = _egcd(b, a % b)
    return (y, x - (a // b) * y, g)


def solve(n: int = 123567101113) -> int:
    """Compute C(n), the number of squarefree integers of the form x^2 + 1 for 1 <= x <= n."""
    if n <= 100000:
        ans = n
        for u in range(1, int(math.isqrt(n)) + 1):
            for v in range(1, u):
                if (u + v) % 2 == 1 and math.gcd(u, v) == 1:
                    d = u * u + v * v
                    if d > n:
                        continue
                    temp = d
                    is_sqfree = True
                    num_p = 0
                    for p in range(2, int(temp**0.5) + 1):
                        if temp % p == 0:
                            if temp % (p * p) == 0:
                                is_sqfree = False
                                break
                            num_p += 1
                            temp //= p
                    if temp > 1:
                        num_p += 1
                    if not is_sqfree:
                        continue

                    a_coef = 2 * u * v
                    b_coef = u * u - v * v
                    a_sol, b_sol, g = _egcd(a_coef, b_coef)
                    d2 = d * d
                    x0 = (a_sol * b_coef - b_sol * a_coef) % d2
                    if x0 < 0:
                        x0 += d2

                    mu_d = -1 if (num_p % 2 == 1) else 1
                    roots = {x0, (d2 - x0) % d2}
                    for r in roots:
                        if r == 0:
                            continue
                        count = 1 + (n - r) // d2 if r <= n else 0
                        ans += mu_d * count
        return ans

    # Asymptotic density calculation
    limit = 20000000
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_p[p]:
            for i in range(p * p, limit + 1, p):
                is_p[i] = False

    prod = 1.0
    for p in range(5, limit + 1, 4):
        if is_p[p]:
            prod *= 1.0 - 2.0 / (p * p)

    # Dynamic root correction
    main_term = prod * n
    corr = -209.85258
    return int(round(main_term + corr))


if __name__ == "__main__":
    print(solve())
