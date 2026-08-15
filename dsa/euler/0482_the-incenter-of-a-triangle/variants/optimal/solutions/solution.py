"""Project Euler Problem 482: The Incenter of a Triangle.

Find S(10^7) = sum L, where L = p + |IA| + |IB| + |IC| over all integer-sided triangles
with incenter I, integer segment lengths IA, IB, IC, and perimeter p <= 10^7.
"""

from array import array
from math import gcd, isqrt
from typing import Tuple


def _build_pythagorean_pairs(
    r_max: int, x_max: int
) -> Tuple[array, array, array, array]:
    counts = array("I", [0]) * (r_max + 1)
    m_limit = isqrt(x_max) + 1

    for m in range(2, m_limit + 1):
        mm = m * m
        for n in range(1, m):
            if ((m - n) & 1) == 0:
                continue
            if gcd(m, n) != 1:
                continue
            a = mm - n * n
            b = 2 * m * n
            if a > b:
                a, b = b, a

            k_max = r_max // a
            kb = x_max // b
            if kb < k_max:
                k_max = kb
            if k_max:
                step = a
                for r in range(step, step * (k_max + 1), step):
                    counts[r] += 1

            k_max = r_max // b
            ka = x_max // a
            if ka < k_max:
                k_max = ka
            if k_max:
                step = b
                for r in range(step, step * (k_max + 1), step):
                    counts[r] += 1

    offsets = array("I", [0]) * (r_max + 2)
    total = 0
    for r in range(1, r_max + 1):
        total += counts[r]
        offsets[r + 1] = total

    xs = array("I", [0]) * total
    us = array("I", [0]) * total
    pos = array("I", offsets)

    for m in range(2, m_limit + 1):
        mm = m * m
        for n in range(1, m):
            if ((m - n) & 1) == 0:
                continue
            if gcd(m, n) != 1:
                continue
            a = mm - n * n
            b = 2 * m * n
            if a > b:
                a, b = b, a
            c = mm + n * n

            k_max = r_max // a
            kb = x_max // b
            if kb < k_max:
                k_max = kb
            for k in range(1, k_max + 1):
                r = k * a
                idx = pos[r]
                xs[idx] = k * b
                us[idx] = k * c
                pos[r] = idx + 1

            k_max = r_max // b
            ka = x_max // a
            if ka < k_max:
                k_max = ka
            for k in range(1, k_max + 1):
                r = k * b
                idx = pos[r]
                xs[idx] = k * a
                us[idx] = k * c
                pos[r] = idx + 1

    return counts, offsets, xs, us


def solve(p_limit: int = 10**7) -> int:
    """Compute S(P) using inradius Pythagorean generation and harmonic cotangent relations."""
    s_max = p_limit // 2
    if s_max < 3:
        return 0

    x_max = s_max - 2
    r_max = int(s_max * (3**0.5) / 9) + 2

    _, offsets, xs, us = _build_pythagorean_pairs(r_max, x_max)
    total = 0

    for r in range(1, r_max + 1):
        start = offsets[r]
        end = offsets[r + 1]
        if end - start < 3:
            continue

        m_dict = {}
        for i in range(start, end):
            m_dict[xs[i]] = us[i]
        if len(m_dict) < 3:
            continue

        x_list = sorted(m_dict)
        r2 = r * r
        m_get = m_dict.get
        n = len(x_list)

        for i in range(n):
            x = x_list[i]
            ux = m_dict[x]
            for j in range(i, n):
                y = x_list[j]
                denom = x * y - r2
                if denom <= 0:
                    continue
                numer = r2 * (x + y)
                if numer % denom != 0:
                    continue
                z = numer // denom
                if z < y:
                    continue
                s = x + y + z
                if s > s_max:
                    continue
                uz = m_get(z)
                if uz is None:
                    continue

                total += 2 * s + ux + m_dict[y] + uz

    return total


if __name__ == "__main__":
    print(solve())
