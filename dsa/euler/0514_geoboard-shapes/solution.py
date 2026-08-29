"""Project Euler Problem 514: Geoboard Shapes.

Calculate E(100) rounded to 5 decimal places, where E(N) is the expected area
of the convex hull formed by randomly placed pins on an order-N square geoboard.
"""

from math import gcd
from typing import List


def solve(n: int = 100) -> str:
    """Compute expected convex hull area E(n) using D4 symmetry and Green's theorem edge expectation."""
    if n <= 0:
        raise ValueError("n must be positive")

    m_size = n + 1
    p = 1.0 / m_size
    q = 1.0 - p
    total_points = m_size * m_size

    qpow: List[float] = [1.0] * (total_points + 1)
    for k in range(1, total_points + 1):
        qpow[k] = qpow[k - 1] * q

    one_minus_qpow: List[float] = [0.0] * (total_points + 1)
    for k in range(total_points + 1):
        one_minus_qpow[k] = 1.0 - qpow[k]

    ky_table: List[List[int]] = [[] for _ in range(n + 1)]
    ky_table[0] = [10**9] * m_size
    for b in range(1, n + 1):
        ky = [0] * m_size
        for y in range(m_size):
            ky[y] = (n - y) // b
        ky_table[b] = ky

    kx_table: List[List[int]] = [[] for _ in range(n + 1)]
    ayoff_table: List[List[int]] = [[] for _ in range(n + 1)]
    for a in range(1, n + 1):
        kx = [0] * m_size
        ayoff = [0] * m_size
        for x in range(m_size):
            kx[x] = (n - x) // a
        for y in range(m_size):
            ayoff[y] = a * (n - y)
        kx_table[a] = kx
        ayoff_table[a] = ayoff

    qpow_small: List[float] = [1.0] * (m_size + 1)
    for k in range(1, m_size + 1):
        qpow_small[k] = qpow_small[k - 1] * q

    p2 = p * p
    p2s: List[float] = [0.0] * (m_size + 1)
    for length in range(2, m_size + 1):
        s = 0.0
        for d in range(1, length):
            s += d * (length - d) * qpow_small[d - 1]
        p2s[length] = p2 * s

    total_cross_scaled = 0.0

    for a in range(1, n + 1):
        kx_a = kx_table[a]
        ay_a = ayoff_table[a]
        for b in range(0, a + 1):
            if gcd(a, b) != 1:
                continue
            if b == 0 and a != 1:
                continue

            mult = 4 if (b == 0 or a == b) else 8

            if b == 0:
                above = 0
                dir_sum = 0.0
                min_t = -a * n
                k0 = 4 * min_t - 2 * n * (b - a)
                k_val = 4 * n + k0
                length = m_size
                coeff_l = p2s[length]
                for _y in range(m_size):
                    below = total_points - above - length
                    dir_sum += (
                        qpow[above]
                        * one_minus_qpow[below]
                        * (k_val * coeff_l)
                    )
                    above += length
                    k_val -= 4
                total_cross_scaled += mult * dir_sum
                continue

            r_distinct = n * (a + b) + 1
            counts = [0] * r_distinct
            ky_b = ky_table[b]

            for x0 in range(a):
                kx_base = kx_a[x0]
                bx = b * x0
                for y0 in range(m_size):
                    ky = ky_b[y0]
                    length = 1 + (kx_base if ky > kx_base else ky)
                    counts[bx + ay_a[y0]] = length

            for x0 in range(a, m_size):
                kx_base = kx_a[x0]
                bx = b * x0
                for y0 in range(b):
                    ky = ky_b[y0]
                    length = 1 + (kx_base if ky > kx_base else ky)
                    counts[bx + ay_a[y0]] = length

            above = 0
            k0 = 4 * (-a * n) - 2 * n * (b - a)
            k_val = 4 * (r_distinct - 1) + k0
            dir_sum = 0.0
            for idx in range(r_distinct - 1, -1, -1):
                cnt = counts[idx]
                if cnt:
                    below = total_points - above - cnt
                    dir_sum += (
                        qpow[above]
                        * one_minus_qpow[below]
                        * (k_val * p2s[cnt])
                    )
                    above += cnt
                k_val -= 4

            total_cross_scaled += mult * dir_sum

    ans = total_cross_scaled / 8.0
    return f"{ans:.5f}"


if __name__ == "__main__":
    print(solve())
