"""Project Euler Problem 404: Crisscross Ellipses.

Find C(10^17), the number of distinct canonical ellipsoidal triplets (a, b, c) for a <= 10^17.
"""

from math import gcd


def solve(limit: int = 10**17) -> int:
    """Compute C(limit) via primitive algebraic parametrization over m and n."""
    m_max = int((2 * limit) ** 0.25) + 1
    total = 0

    for m in range(1, m_max + 1):
        m2 = m * m

        # Branch 1: n in (-m/3, 0)
        n_start = -(m // 3)
        if m % 3 == 0:
            n_start += 1
        for n in range(n_start, 0):
            if (m & 1) and (n & 1):
                continue
            if (m - 2 * n) % 5 == 0:
                continue
            if gcd(m, -n) != 1:
                continue

            n2 = n * n
            mn = m * n
            p = m2 - n2 - 4 * mn
            r = m2 - n2 + mn
            a0 = p * r
            if a0 <= limit:
                total += limit // a0

        # Branch 2: n in (m/2, m)
        for n in range(m // 2 + 1, m):
            if (m & 1) and (n & 1):
                continue
            if (m - 2 * n) % 5 == 0:
                continue
            if gcd(m, n) != 1:
                continue

            n2 = n * n
            mn = m * n
            p = n2 + 4 * mn - m2
            r = m2 - n2 + mn
            a0 = p * r
            if a0 <= limit:
                total += limit // a0

    return total


if __name__ == "__main__":
    print(solve())
