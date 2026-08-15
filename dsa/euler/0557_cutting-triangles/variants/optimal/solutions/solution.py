"""Project Euler Problem 557: Cutting Triangles.

Find S(10000), where S(n) is the sum of total triangle areas a+b+c+d <= n
across all valid integer triangle cutting quadruples (a, b, c, d) with b <= c.
"""

from math import gcd, isqrt


def _is_square(x: int) -> int:
    if x < 0:
        return -1
    r = isqrt(x)
    return r if r * r == x else -1


def solve(limit_n: int = 10_000) -> int:
    """Compute S(limit_n) using (s, a, d) substitution and quadratic discriminant resolution."""
    total_sum = 0

    for s in range(3, 2 * limit_n + 1):
        a_min = max(1, s - limit_n)
        a_max = (s - 3) // 2

        if a_min > a_max:
            continue

        for a in range(a_min, a_max + 1):
            a2 = a * a
            g = gcd(s, a2)
            if g == 1:
                continue

            step = s // g
            max_k = (s - 2 * a - 2) // step
            if max_k <= 0:
                continue

            base_prod = a2 // g

            for k in range(1, max_k + 1):
                d = step * k
                w = s - 2 * a - d
                prod = base_prod * k

                disc = w * w - 4 * prod
                r = _is_square(disc)
                if r < 0:
                    continue

                if (w - r) & 1:
                    continue

                b = (w - r) // 2
                if b <= 0:
                    continue
                c = (w + r) // 2
                if b > c:
                    continue

                t = s - a
                total_sum += t

    return total_sum


if __name__ == "__main__":
    print(solve())
