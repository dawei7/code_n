"""Project Euler Problem 785: Symmetric Diophantine Equation.

Find S(10^9), the sum of x + y + z over all primitive solutions of
15(x^2 + y^2 + z^2) = 34(xy + yz + zx) with 1 <= x <= y <= z <= N.
"""

import math
from typing import List


def _solve(N: int) -> int:
    max_a = math.isqrt(N // 3)

    spf = list(range(max_a + 1))
    for i in range(2, int(math.isqrt(max_a)) + 1):
        if spf[i] == i:
            step = i
            start = i * i
            for j in range(start, max_a + 1, step):
                if spf[j] == j:
                    spf[j] = i

    def distinct_prime_factors(x: int) -> List[int]:
        res = []
        while x > 1:
            p = spf[x]
            res.append(p)
            while x % p == 0:
                x //= p
        return res

    total = 0
    N3 = 12 * N
    N5 = 5 * N

    for a in range(1, max_a + 1):
        aa = a * a
        pf = distinct_prime_factors(a)

        if 5 * aa <= N:
            bmin = 1
        else:
            num = 5 * aa - N
            bmin = (num + (2 * a - 1)) // (2 * a)
            if bmin < 1:
                bmin = 1

        bmax_pos = (3 * a - 1) // 5
        if bmax_pos < bmin:
            continue

        disc1 = 4 * aa + N3
        bmax1 = (-2 * a + math.isqrt(disc1)) // 6

        disc3 = aa + N5
        sdisc3 = math.isqrt(disc3)
        bmax3 = (4 * a + sdisc3) // 5
        bmin3 = (4 * a - sdisc3 + 4) // 5

        if bmin3 > bmin:
            bmin = bmin3

        bmax = bmax_pos
        if bmax1 < bmax:
            bmax = bmax1
        if bmax3 < bmax:
            bmax = bmax3
        if bmax >= a:
            bmax = a - 1

        if bmax < bmin:
            continue

        for b in range(bmin, bmax + 1):
            ok = True
            for p in pf:
                if b % p == 0:
                    ok = False
                    break
            if not ok:
                continue

            ab = a * b
            bb = b * b

            A = 2 * ab + 3 * bb
            B = 5 * aa - 2 * ab
            C = 3 * aa - 8 * ab + 5 * bb

            if C <= 0 or A > N or B > N or C > N:
                continue

            if A % 19 == 0 and B % 19 == 0:
                continue

            total += 8 * (aa - ab + bb)

    return total


def solve(N: int = 1_000_000_000) -> int:
    """Compute S(N) using coprime parameterization of the symmetric ternary quadratic form."""
    ans = 0
    for _iter in range(1):
        ans = _solve(N)
    return ans


if __name__ == "__main__":
    print(solve())
