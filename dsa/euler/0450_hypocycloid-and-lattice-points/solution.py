"""Project Euler Problem 450: Hypocycloid and Lattice Points.

Find T(10^6), the sum of |x| + |y| over all distinct integer-coordinate points
on hypocycloids with rational sin(t) and cos(t) for R <= N and 2r < R.
"""

from math import gcd, isqrt
from typing import Dict, List, Set, Tuple


def _mobius_sieve(n: int) -> List[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: List[int] = []
    is_comp = [False] * (n + 1)
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            ip = i * p
            if ip > n:
                break
            is_comp[ip] = True
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]
    return mu


def _build_prefix(
    mu: List[int],
) -> Tuple[List[int], List[int], List[int], List[int]]:
    n = len(mu) - 1
    pref_mu = [0] * (n + 1)
    pref_mui = [0] * (n + 1)
    pref_mu_odd = [0] * (n + 1)
    pref_mui_odd = [0] * (n + 1)

    s0 = s1 = so0 = so1 = 0
    for i in range(1, n + 1):
        mi = mu[i]
        s0 += mi
        s1 += mi * i
        if i & 1:
            so0 += mi
            so1 += mi * i
        pref_mu[i] = s0
        pref_mui[i] = s1
        pref_mu_odd[i] = so0
        pref_mui_odd[i] = so1
    return pref_mu, pref_mui, pref_mu_odd, pref_mui_odd


def _g0(n: int) -> int:
    if n <= 2:
        return 0
    m = (n - 1) // 2
    return m * (n - m - 1)


def _ga(n: int) -> int:
    c = _g0(n)
    return (n + 1) * c // 2


def _gb(n: int) -> int:
    if n <= 2:
        return 0
    m = (n - 1) // 2
    term = m * (m + 1)
    return term * (3 * n - 4 * m - 2) // 6


def _hb(n: int) -> int:
    m_val = (n - 2) // 2
    if m_val <= 0:
        return 0
    m0 = (m_val - 1) // 2
    if m0 < 0:
        return 0
    s_y = m0 * (m0 + 1) // 2
    s_y2 = m0 * (m0 + 1) * (2 * m0 + 1) // 6
    return m_val * (m0 + 1) * (m0 + 1) - 4 * s_y2 - 2 * s_y


def _kb(n: int) -> int:
    res = 0
    m1 = (n - 2) // 4
    if m1 > 0:
        m1_half = (m1 - 1) // 2
        if m1_half >= 0:
            s_y = m1_half * (m1_half + 1) // 2
            s_y2 = m1_half * (m1_half + 1) * (2 * m1_half + 1) // 6
            sum_4y1 = (m1_half + 1) * (2 * m1_half + 1)
            res += m1 * sum_4y1 - 8 * s_y2 - 2 * s_y

    m3 = (n - 6) // 4
    if m3 > 0:
        m3_half = (m3 - 1) // 2
        if m3_half >= 0:
            s_y = m3_half * (m3_half + 1) // 2
            s_y2 = m3_half * (m3_half + 1) * (2 * m3_half + 1) // 6
            sum_4y3 = (m3_half + 1) * (2 * m3_half + 3)
            res += m3 * sum_4y3 - 8 * s_y2 - 6 * s_y

    return res


def _mobius_sum_weighted(m: int, pref_mui: List[int], base_func) -> int:
    res = 0
    l_idx = 1
    while l_idx <= m:
        q = m // l_idx
        r = m // q
        res += (pref_mui[r] - pref_mui[l_idx - 1]) * base_func(q)
        l_idx = r + 1
    return res


class _AxisCalculator:

    def __init__(self, n: int) -> None:
        mu = _mobius_sieve(n)
        _, pref_mui, _, pref_mui_odd = _build_prefix(mu)
        self.pref_mui = pref_mui
        self.pref_mui_odd = pref_mui_odd
        self.cache: Dict[int, int] = {}

    def f(self, m: int) -> int:
        if m in self.cache:
            return self.cache[m]
        sa = _mobius_sum_weighted(m, self.pref_mui, _ga)
        sb = _mobius_sum_weighted(m, self.pref_mui, _gb)
        p2 = _mobius_sum_weighted(m, self.pref_mui_odd, _hb)
        p4 = _mobius_sum_weighted(m, self.pref_mui_odd, _kb)
        val = 4 * sa + 2 * sb + 2 * p2 - 4 * p4
        self.cache[m] = val
        return val

    def total(self, n: int) -> int:
        total = 0
        l_idx = 1
        while l_idx <= n:
            q = n // l_idx
            r = n // q
            sum_d = (l_idx + r) * (r - l_idx + 1) // 2
            total += sum_d * self.f(q)
            l_idx = r + 1
        return total


def _primitive_triples(cmax: int) -> List[Tuple[int, int, int]]:
    triples: List[Tuple[int, int, int]] = []
    m_limit = isqrt(cmax * 2) + 3
    for m in range(2, m_limit + 1):
        mm = m * m
        for n in range(1, m):
            if ((m - n) & 1) == 0:
                continue
            if gcd(m, n) != 1:
                continue
            c = mm + n * n
            if c > cmax:
                break
            a = mm - n * n
            b = 2 * m * n
            triples.append((a, b, c))
    return triples


def _gauss_pow(re: int, im: int, exp: int) -> Tuple[int, int]:
    rr, ri = 1, 0
    br, bi = re, im
    e = exp
    while e > 0:
        if e & 1:
            rr, ri = rr * br - ri * bi, rr * bi + ri * br
        br, bi = br * br - bi * bi, br * bi + bi * br
        e //= 2
    return rr, ri


def _non_axis_total(n: int) -> int:
    total = 0
    max_a = 1
    while pow(3, max_a + 1) <= n:
        max_a += 1

    for ap in range(2, max_a + 1):
        cmax = int(n ** (1.0 / ap)) + 2
        while pow(cmax, ap) > n:
            cmax -= 1
        triples = _primitive_triples(cmax)

        for bp in range(1, ap):
            if gcd(ap, bp) != 1:
                continue

            for a, b, c in triples:
                den = pow(c, ap)
                if den * (ap + bp) > n:
                    continue

                variants: Set[Tuple[int, int]] = set()
                for u, v in ((a, b), (b, a)):
                    for su in (1, -1):
                        for sv in (1, -1):
                            variants.add((su * u, sv * v))

                for re, im in variants:
                    ua, va = _gauss_pow(re, im, ap)
                    ub, vb = _gauss_pow(re, im, bp)
                    scale = pow(c, ap - bp)

                    num_x = ap * ub * scale + bp * ua
                    num_y = ap * vb * scale - bp * va

                    g = gcd(den, gcd(abs(num_x), abs(num_y)))
                    d0 = den // g
                    if d0 * (ap + bp) > n:
                        continue

                    x0 = num_x // g
                    y0 = num_y // g

                    kmax = n // (d0 * (ap + bp))
                    total += (abs(x0) + abs(y0)) * (
                        kmax * (kmax + 1) // 2
                    )

    return total


def solve(n: int = 1_000_000) -> int:
    """Compute T(n) using Möbius-blocked axis decomposition and Pythagorean Gaussian powers."""
    axis = _AxisCalculator(n).total(n)
    non_axis = _non_axis_total(n)
    channel_totals = [axis, non_axis]
    return sum(val for val in channel_totals)


if __name__ == "__main__":
    print(solve())
