"""Project Euler 261: Pivotal Square Sums

Find the sum of all distinct square-pivots k <= 10^10 such that:
(k - m)^2 + ... + k^2 = (n + 1)^2 + ... + (n + m)^2 for some m > 0 and n >= k.
"""

from __future__ import annotations

import math


def solve(max_k: int = 10**10) -> str:
    """Finds the sum of all distinct square-pivots k <= max_k using generalized Pell equation

    transformations over the recurrence (m+1)k(k-m) = mn(n+m+1).
    """
    pivots: set[int] = set()
    max_m = int((max_k / 2) ** 0.5) + 1

    for m in range(1, max_m + 1):
        d = m * (m + 1)
        u = 2 * m + 1
        v = 2

        # Square-free factorization of m = b * t^2
        t = 1
        temp = m
        for p in range(2, int(m**0.5) + 1):
            if temp % (p * p) == 0:
                while temp % (p * p) == 0:
                    t *= p
                    temp //= p * p
        b = temp
        step = b * t

        # Find all fundamental base solutions (U0, x0) to U^2 - d*x^2 = m*d
        bases: list[tuple[int, int]] = []
        for cap_k in range(0, m // step + 1):
            x0 = step * cap_k
            val = (m + 1) * ((m + x0 * x0) // m)
            w = math.isqrt(val)
            if w * w == val:
                u0 = m * w
                bases.append((u0, x0))
                if 0 < x0 < m:
                    bases.append((u0, -x0))

        # Generate solutions via the fundamental unit (2m+1) + 2*sqrt(d)
        for u0, x0 in bases:
            curr_u, curr_x = u0, x0
            while True:
                next_u = u * curr_u + v * d * curr_x
                next_x = v * curr_u + u * curr_x
                curr_u, curr_x = next_u, next_x

                if curr_x > 0:
                    if (curr_x + m) % 2 == 0:
                        k = (curr_x + m) // 2
                        if k > max_k:
                            break
                        if k > m:
                            if (
                                curr_u % m == 0
                                and (curr_u // m + m + 1) % 2 == 0
                            ):
                                n = (curr_u // m - m - 1) // 2
                                if n >= k:
                                    pivots.add(k)
                    else:
                        if (curr_x + m) // 2 > max_k:
                            break
                elif -curr_x > max_k:
                    break

    return str(sum(pivots))


if __name__ == "__main__":
    print(solve())
