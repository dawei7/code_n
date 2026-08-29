"""Project Euler Problem 843: Periodic Circles.

Mathematical reduction:
Consider a circle of n integers evolving under x_i^{(t+1)} = |x_{i-1}^{(t)} - x_{i+1}^{(t)}|.
Any integer circle eventually settles into an attractor equivalent to a binary state in F_2^n
scaled by an integer constant.

The evolution on F_2^n is a linear operator:
  v_{t+1}(x) = (x + x^{n-1}) v_t(x) mod (x^n - 1)
in the polynomial ring F_2[x] / (x^n - 1).

Decomposing n = 2^a * m with m odd:
  x^n - 1 = (x^m - 1)^{2^a} = (prod_{M | m} Phi_M(x))^{2^a}.

For each divisor M | m, the cyclotomic polynomial Phi_M(x) factors into irreducible
polynomials of degree d = ord_M(2) over F_2.
In each irreducible component f | Phi_M, the operator g(x) = x + x^{M-1} has a base
multiplicative order ord_f(g) dividing 2^{d_beta} - 1, where d_beta is the order of 2
in (Z/M Z)* / {+-1}.

The possible period lengths for a given n are all LCMs of subsets of:
  { ord_f(g) * 2^k  |  f | Phi_M(x), M | m, M > 1, 0 <= k <= a }.

The sum S(N) of all unique periods across 3 <= n <= N is computed in O(N log^2 N) time.
"""

from __future__ import annotations

import math


def poly_deg(a: int) -> int:
    return a.bit_length() - 1


def poly_mod(a: int, b: int) -> int:
    deg_b = poly_deg(b)
    if deg_b < 0:
        raise ZeroDivisionError
    deg_a = poly_deg(a)
    while deg_a >= deg_b:
        a ^= b << (deg_a - deg_b)
        deg_a = poly_deg(a)
    return a


def poly_div(a: int, b: int) -> int:
    deg_b = poly_deg(b)
    q = 0
    while poly_deg(a) >= deg_b:
        shift = poly_deg(a) - deg_b
        q ^= 1 << shift
        a ^= b << shift
    return q


def poly_mul(a: int, b: int) -> int:
    res = 0
    while b > 0:
        if b & 1:
            res ^= a
        a <<= 1
        b >>= 1
    return res


def poly_pow_mod(base: int, exp: int, mod: int) -> int:
    res = 1
    base = poly_mod(base, mod)
    while exp > 0:
        if exp & 1:
            res = poly_mod(poly_mul(res, base), mod)
        base = poly_mod(poly_mul(base, base), mod)
        exp >>= 1
    return res


def poly_gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, poly_mod(a, b)
    return a


def solve(max_n: int = 100) -> int:
    """Compute S(max_n) in O(max_n * log^2 max_n) time."""
    cyclo_cache: dict[int, int] = {}

    def get_cyclotomic(m_val: int) -> int:
        if m_val not in cyclo_cache:
            poly = (1 << m_val) ^ 1
            for d in range(1, m_val):
                if m_val % d == 0:
                    poly = poly_div(poly, get_cyclotomic(d))
            cyclo_cache[m_val] = poly
        return cyclo_cache[m_val]

    m_base_orders: dict[int, list[int]] = {}

    def get_base_orders_for_m(m_val: int) -> list[int]:
        if m_val == 1:
            return []
        if m_val in m_base_orders:
            return m_base_orders[m_val]

        d = 1
        while pow(2, d, m_val) != 1:
            d += 1
        phi_m = get_cyclotomic(m_val)

        factors = [phi_m]
        t_cand = 2
        while not all(poly_deg(f) == d for f in factors):
            new_factors = []
            for f in factors:
                if poly_deg(f) == d:
                    new_factors.append(f)
                    continue
                tr = 0
                term = poly_mod(t_cand, f)
                for _ in range(d):
                    tr ^= term
                    term = poly_pow_mod(term, 2, f)
                g = poly_gcd(tr, f)
                if 1 < g < f:
                    new_factors.append(g)
                    new_factors.append(poly_div(f, g))
                else:
                    new_factors.append(f)
            factors = new_factors
            t_cand += 1
            if t_cand & 1 == 0:
                t_cand += 1

        d_beta = 1
        while (pow(2, d_beta, m_val) != 1) and (pow(2, d_beta, m_val) != m_val - 1):
            d_beta += 1

        max_ord = (1 << d_beta) - 1
        temp = max_ord
        p_facs = []
        p = 2
        while p * p <= temp:
            if temp % p == 0:
                p_facs.append(p)
                while temp % p == 0:
                    temp //= p
            p += 1
        if temp > 1:
            p_facs.append(temp)

        base_orders = set()
        g = poly_mod((1 << 1) ^ (1 << (m_val - 1)), phi_m)
        for f in factors:
            gf = poly_mod(g, f)
            if gf == 0:
                continue
            ord_g = max_ord
            for p_div in p_facs:
                while ord_g % p_div == 0 and poly_pow_mod(gf, ord_g // p_div, f) == 1:
                    ord_g //= p_div
            base_orders.add(ord_g)

        m_base_orders[m_val] = list(base_orders)
        return m_base_orders[m_val]

    def periods_for_n(n: int) -> set[int]:
        a = 0
        m = n
        while m % 2 == 0:
            a += 1
            m //= 2
        if m == 1:
            return {1}

        base_orders = set()
        for m_div in range(2, m + 1):
            if m % m_div == 0:
                base_orders.update(get_base_orders_for_m(m_div))

        all_terms = []
        for bo in base_orders:
            for k in range(a + 1):
                all_terms.append(bo * (1 << k))

        all_lcms = {1}
        for term in all_terms:
            next_lcms = set(all_lcms)
            for cur in all_lcms:
                next_lcms.add(math.lcm(cur, term))
            all_lcms = next_lcms
        return all_lcms

    all_periods: set[int] = set()
    for n in range(3, max_n + 1):
        all_periods.update(periods_for_n(n))

    return sum(all_periods)


if __name__ == "__main__":
    print(solve())
