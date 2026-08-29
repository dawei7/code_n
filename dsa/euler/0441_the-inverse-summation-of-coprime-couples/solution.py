"""Project Euler Problem 441: The Inverse Summation of Coprime Couples.

Find S(10^7) rounded to four decimal places.
"""

from array import array
from typing import Dict, List, Tuple


def _mobius_sieve(limit: int) -> array:
    mu = array("b", [0]) * (limit + 1)
    mu[1] = 1
    is_comp = bytearray(limit + 1)
    primes: List[int] = []

    for i in range(2, limit + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            ip = i * p
            if ip > limit:
                break
            is_comp[ip] = 1
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]
    return mu


def _harmonic_arrays(n: int) -> Tuple[array, array]:
    h_arr = array("d", [0.0]) * (n + 1)
    h2_arr = array("d", [0.0]) * (n + 1)

    h_val = 0.0
    c_val = 0.0
    h2_val = 0.0
    c2_val = 0.0

    for i in range(1, n + 1):
        inv = 1.0 / i

        y = inv - c_val
        t = h_val + y
        c_val = (t - h_val) - y
        h_val = t
        h_arr[i] = h_val

        inv2 = inv * inv
        y2 = inv2 - c2_val
        t2 = h2_val + y2
        c2_val = (t2 - h2_val) - y2
        h2_val = t2
        h2_arr[i] = h2_val

    return h_arr, h2_arr


def solve(n: int = 10_000_000) -> str:
    """Compute S(n) rounded to four decimal places using Möbius inversion and Kahan harmonic prefix sums."""
    half = n // 2
    mu = _mobius_sieve(half)
    h_arr, h2_arr = _harmonic_arrays(n)

    def p1_func(t: int) -> float:
        if t <= 0:
            return 0.0
        ht = h_arr[t]
        return 0.5 * (ht * ht - h2_arr[t])

    def sum_h(t: int) -> float:
        if t <= 0:
            return 0.0
        return (t + 1) * h_arr[t] - t

    def sum_hm1(t: int) -> float:
        if t <= 1:
            return 0.0
        return t * h_arr[t - 1] - (t - 1)

    s_phi_over_q = 0.0
    s_btotal_over_q = 0.0

    for d in range(1, half + 1):
        md = mu[d]
        if md == 0:
            continue
        inv_d = 1.0 / d
        inv_d2 = inv_d * inv_d
        k = half // d
        s_phi_over_q += md * k * inv_d
        s_btotal_over_q += md * p1_func(k) * inv_d2

    s_phi_over_q -= 1.0

    s_a = 0.0
    s_weighted_btotal = 0.0
    s_b_combined = 0.0

    s2_cache: Dict[Tuple[int, int], float] = {}

    def s2_prefix(m_val: int, l_val: int) -> float:
        if l_val <= 0:
            return 0.0
        key = (m_val, l_val)
        cached = s2_cache.get(key)
        if cached is not None:
            return cached
        s_res = 0.0
        denom = m_val - 1
        for r in range(1, l_val + 1):
            s_res += h_arr[r] / denom
            denom -= 1
        s2_cache[key] = s_res
        return s_res

    for d in range(1, half + 1):
        md = mu[d]
        if md == 0:
            continue
        inv_d = 1.0 / d
        inv_d2 = inv_d * inv_d

        m_val = n // d
        a_val = n // (2 * d) + 1

        inner_a = m_val * (h_arr[m_val] - h_arr[a_val - 1]) - (
            m_val - a_val + 1
        )
        s_a += md * inner_a * inv_d

        s_over_k = p1_func(m_val) - p1_func(a_val - 1)
        s_hm1_val = sum_hm1(m_val) - sum_hm1(a_val - 1)
        s_weighted_btotal += md * (
            (n + 1) * s_over_k * inv_d2 - s_hm1_val * inv_d
        )

        l_val = m_val - a_val
        s_rev = sum_h(l_val)
        s2_val = s2_prefix(m_val, l_val)
        s_b_combined += md * (s_rev * inv_d - n * s2_val * inv_d2)

    total = (
        s_phi_over_q
        + s_btotal_over_q
        + s_a
        + s_weighted_btotal
        + s_b_combined
    )
    return f"{total:.4f}"


if __name__ == "__main__":
    print(solve())
