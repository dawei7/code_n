"""Project Euler Problem 476: Circle Packing II.

Find S(1803), the average maximum area covered by three non-overlapping circles
inside an integer triangle (a, b, c) with 1 <= a <= b <= c < a + b <= 1803,
rounded to 5 decimal places.
"""

from math import pi, sqrt


def _count_triangles(n: int) -> int:
    m = n // 2
    return sum(a * (n - 2 * a + 1) for a in range(1, m + 1))


def solve(n: int = 1803) -> str:
    """Compute S(n) using optimal Zalgaller-Los 3-circle packing geometry."""
    total_count = _count_triangles(n)
    total = 0.0
    n2 = n // 2

    for a in range(1, n2 + 1):
        twoa = 2 * a
        foura = 4 * a
        for b in range(a, n - a + 1):
            s_ab = a + b
            twos = 2 * s_ab
            twob = 2 * b
            fourb = 4 * b

            for x in range(1, a + 1):
                c = s_ab - x
                t1 = twoa - x
                t2 = twob - x
                r2 = (x * t1 * t2) / (4.0 * (twos - x))

                s_a = sqrt((x * t1) / (fourb * c))
                k_a = (1.0 - s_a) / (1.0 + s_a)
                k_a2 = k_a * k_a

                s_b = sqrt((x * t2) / (foura * c))

                if s_b <= (2.0 * s_a) / (1.0 + s_a * s_a):
                    k_b = (1.0 - s_b) / (1.0 + s_b)
                    k_b2 = k_b * k_b
                    factor = 1.0 + k_a2 + k_b2
                else:
                    factor = 1.0 + k_a2 + k_a2 * k_a2

                total += r2 * factor

    ans = pi * total / total_count
    return f"{ans:.5f}"


if __name__ == "__main__":
    print(solve())
