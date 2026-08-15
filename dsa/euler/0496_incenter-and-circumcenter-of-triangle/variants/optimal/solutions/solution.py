"""Project Euler Problem 496: Incenter and Circumcenter of Triangle.

Find F(10^9), the sum of side BC over all integer-sided triangles ABC
satisfying AC = DI and BC <= 10^9 (where I is the incenter and D is the circumcircle intersection of AI).
"""

from math import isqrt
from typing import List, Tuple


def _build_spf(n: int) -> List[int]:
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    lim = isqrt(n)
    for i in range(2, lim + 1):
        if spf[i] == i:
            step = i
            start = i * i
            for j in range(start, n + 1, step):
                if spf[j] == j:
                    spf[j] = i
    return spf


def _squarefree_divs_mu_times_d(
    p: int, spf: List[int]
) -> List[Tuple[int, int]]:
    primes: List[int] = []
    x = p
    while x > 1:
        pr = spf[x]
        primes.append(pr)
        while x % pr == 0:
            x //= pr

    divs: List[Tuple[int, int]] = [(1, 1)]
    for pr in primes:
        current = divs[:]
        for d, coef in current:
            divs.append((d * pr, -coef * pr))
    return divs


def _coprime_prefix_sum(
    divs_mu_d: List[Tuple[int, int]], x: int
) -> int:
    if x <= 0:
        return 0
    total = 0
    for d, coef in divs_mu_d:
        n = x // d
        total += coef * (n * (n + 1) // 2)
    return total


def solve(limit_l: int = 10**9) -> int:
    """Compute F(L) using Mobius inversion and quotient hyperbola batching."""
    p_max = isqrt(limit_l) + 1
    spf = _build_spf(p_max)
    div_lists: List[List[Tuple[int, int]]] = [[] for _ in range(p_max + 1)]
    div_lists[1] = [(1, 1)]
    for p in range(2, p_max + 1):
        div_lists[p] = _squarefree_divs_mu_times_d(p, spf)

    ans = 0
    for p in range(1, p_max + 1):
        q_low = p + 1
        q_high = min(2 * p - 1, limit_l // p)
        if q_low > q_high:
            continue

        m_val = limit_l // p
        divs_mu_d = div_lists[p]

        q = q_low
        while q <= q_high:
            v = m_val // q
            q_end = min(q_high, m_val // v)

            sum_q = _coprime_prefix_sum(
                divs_mu_d, q_end
            ) - _coprime_prefix_sum(divs_mu_d, q - 1)
            if sum_q:
                tri = v * (v + 1) // 2
                ans += p * tri * sum_q

            q = q_end + 1

    return ans


if __name__ == "__main__":
    print(solve())
