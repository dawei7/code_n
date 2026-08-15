"""Project Euler Problem 611: Hallway of Square Steps.

Find F(10^12), where F(N) is the number of doors left open after toggling doors
for each representation n = a^2 + b^2 with 1 <= a < b.
"""

from array import array
from math import isqrt
from typing import List, Tuple


def _sieve_spf(n: int) -> Tuple[array, List[int]]:
    spf = array("I", [0]) * (n + 1)
    primes: List[int] = []
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            ip = i * p
            if ip > n:
                break
            spf[ip] = p
            if p == spf[i]:
                break
    return spf, primes


def _build_pi1_prefix(limit: int, primes: List[int]) -> array:
    is_p = bytearray(limit + 1)
    for p in primes:
        if p <= limit:
            is_p[p] = 1

    pi1 = array("I", [0]) * (limit + 1)
    c = 0
    for x in range(limit + 1):
        if is_p[x] and (x & 3) == 1:
            c += 1
        pi1[x] = c
    return pi1


def _pi_and_char(
    n: int, primes: List[int], root: int
) -> Tuple[array, array, array, array]:
    vals = array("q")
    i = 1
    while i <= n:
        q = n // i
        vals.append(q)
        i = n // q + 1

    m = len(vals)
    idx_big = array("I", [0]) * (root + 1)
    for idx, v in enumerate(vals):
        if v > root:
            idx_big[n // v] = idx
        else:
            break

    pi = array("q", [0]) * m
    schi = array("q", [0]) * m
    for j in range(m):
        v = vals[j]
        if v >= 2:
            pi[j] = v - 1
        s_int = ((v + 3) // 4) - ((v + 1) // 4)
        schi[j] = s_int - 1

    def upper_bound(threshold: int) -> int:
        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi) // 2
            if vals[mid] >= threshold:
                lo = mid + 1
            else:
                hi = mid
        return lo

    vals_l = vals
    pi_l = pi
    schi_l = schi
    idx_big_l = idx_big
    m_l = m
    root_l = root
    n_l = n

    for p in primes:
        p2 = p * p
        if p2 > n_l:
            break
        k = upper_bound(p2)
        if k == 0:
            break

        base_idx = m_l - (p - 1)
        base_pi = pi_l[base_idx]
        base_s = schi_l[base_idx]
        chi_p = 0 if p == 2 else (1 if (p & 3) == 1 else -1)

        for j in range(k):
            v = vals_l[j]
            vp = v // p
            if vp <= root_l:
                idx_vp = m_l - vp
            else:
                idx_vp = idx_big_l[n_l // vp]

            pi_l[j] -= pi_l[idx_vp] - base_pi
            if chi_p:
                schi_l[j] -= chi_p * (schi_l[idx_vp] - base_s)

    return vals, idx_big, pi, schi


def _parity_and_excluded_primes(
    u: int, spf: array
) -> Tuple[int, List[int]]:
    parity = 0
    excluded: List[int] = []
    while u > 1:
        p = spf[u]
        odd = 0
        while u % p == 0:
            u //= p
            odd ^= 1
        if odd and (p & 3) == 1:
            parity ^= 1
            excluded.append(p)
    return parity, excluded


def solve(n: int = 10**12) -> int:
    """Compute F(N) using Legendre prime summatory counting for primes p = 1 (mod 4)."""
    root = isqrt(n)
    spf, primes = _sieve_spf(root)
    pi1_small = _build_pi1_prefix(root, primes)

    vals, idx_big, pi_tab, schi_tab = _pi_and_char(n, primes, root)

    def pi1_query(x: int) -> int:
        if x < 5:
            return 0
        if x <= root:
            return int(pi1_small[x])
        i = n // x
        idx = idx_big[i]
        pi_x = pi_tab[idx]
        s_x = schi_tab[idx]
        return int((pi_x - 1 + s_x) // 2)

    total = 0

    for u in range(1, root + 1, 2):
        u2 = u * u
        max2 = n // u2
        parity, excluded = _parity_and_excluded_primes(u, spf)

        if parity:
            total += max2.bit_length()

        x = max2
        while x >= 5:
            cnt = pi1_query(x)
            if excluded:
                ex = 0
                for p in excluded:
                    if p <= x:
                        ex += 1
                    else:
                        break
                cnt -= ex
            total += cnt
            x //= 2

    return total


if __name__ == "__main__":
    print(solve())
