"""Project Euler Problem 420: 2x2 Positive Integer Matrix.

Find F(10^7), the number of 2x2 positive integer matrices with trace < 10^7 that can be
expressed as the square of a positive integer matrix in two different ways.
"""

from array import array
from math import gcd, isqrt
from typing import List, Optional


def _divisor_counts_upto_linear(m_val: int) -> array:
    spf = array("I", [0]) * (m_val + 1)
    d = array("I", [0]) * (m_val + 1)
    exp = array("B", [0]) * (m_val + 1)
    primes: List[int] = []

    d[1] = 1
    for i in range(2, m_val + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
            exp[i] = 1
            d[i] = 2

        si = spf[i]
        di = d[i]
        ei = exp[i]

        for p in primes:
            ip = i * p
            if ip > m_val:
                break
            spf[ip] = p
            if p == si:
                exp[ip] = ei + 1
                d[ip] = di // (ei + 1) * (exp[ip] + 1)
                break
            else:
                exp[ip] = 1
                d[ip] = di * 2

    return d


def solve(n_val: int = 10_000_000) -> int:
    """Compute F(n_val) by summing divisor counts over valid parameter ranges for trace u^2 + v^2 < n_val."""
    umax = isqrt(n_val - 2)
    kmax = 2 * umax
    m_val = (kmax * kmax) // 4

    d = _divisor_counts_upto_linear(m_val)

    prefix: List[Optional[array]] = [None] * (kmax + 1)
    for k in range(2, kmax + 1):
        pref = array("I", [0]) * k
        s = 0
        for a in range(1, k):
            s += d[a * (k - a)]
            pref[a] = s
        prefix[k] = pref

    total = 0

    for u in range(2, umax + 1):
        vmax = isqrt(n_val - 1 - u * u)
        if vmax >= u:
            vmax = u - 1
        for v in range(1, vmax + 1):
            g = gcd(u, v)
            uu = u // g
            vv = v // g

            delta = 2 if ((uu & 1) and (vv & 1)) else 1
            k = g * delta
            if k <= 1:
                continue

            s = u + v
            low = (v * k) // s + 1
            high = (u * k - 1) // s

            if low < 1:
                low = 1
            if high > k - 1:
                high = k - 1

            if low <= high:
                pref = prefix[k]
                assert pref is not None
                total += pref[high] - pref[low - 1]

    return total


if __name__ == "__main__":
    print(solve())
