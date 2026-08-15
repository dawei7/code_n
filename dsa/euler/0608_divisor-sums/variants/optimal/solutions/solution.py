"""Project Euler Problem 608: Divisor Sums.

Find D(200!, 10^12) mod 1000000007, where D(m, n) = sum_{d | m} sum_{k=1}^n sigma_0(k * d).
"""

import bisect
from collections import defaultdict
import math
from typing import Dict, List, Tuple

_MOD = 1_000_000_007


def _primes_upto(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    r = int(n**0.5)
    for i in range(2, r + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start : n + 1 : step] = b"\x00" * (
                ((n - start) // step) + 1
            )
    return [i for i in range(2, n + 1) if sieve[i]]


def _v_factorial(n: int, p: int) -> int:
    e = 0
    while n:
        n //= p
        e += n
    return e


def _tau_prefix_summatory(b_limit: int) -> List[int]:
    if b_limit <= 0:
        return [0]
    lp = [0] * (b_limit + 1)
    exp = [0] * (b_limit + 1)
    tau = [0] * (b_limit + 1)
    primes: List[int] = []
    tau[1] = 1

    for i in range(2, b_limit + 1):
        if lp[i] == 0:
            lp[i] = i
            exp[i] = 1
            tau[i] = 2
            primes.append(i)
        for p in primes:
            ip = i * p
            if ip > b_limit:
                break
            lp[ip] = p
            if p == lp[i]:
                exp[ip] = exp[i] + 1
                tau[ip] = (tau[i] // (exp[i] + 1)) * (exp[i] + 2)
                break
            exp[ip] = 1
            tau[ip] = tau[i] * 2

    pref = [0] * (b_limit + 1)
    s = 0
    for i in range(1, b_limit + 1):
        s += tau[i]
        pref[i] = s
    return pref


def _t_summatory(
    n: int, pref_small: List[int], b_limit: int, cache: Dict[int, int]
) -> int:
    if n <= b_limit:
        return pref_small[n]
    if n in cache:
        return cache[n]
    r = int(math.isqrt(n))
    s = 0
    for i in range(1, r + 1):
        s += n // i
    res = 2 * s - r * r
    cache[n] = res
    return res


def _gen_products_weights(
    primes: List[int], weights: List[int], limit: int
) -> Tuple[List[int], List[int]]:
    prods: List[int] = []
    wgts: List[int] = []
    stack = [(0, 1, 1)]
    l_len = len(primes)

    while stack:
        i, prod, w = stack.pop()
        prods.append(prod)
        wgts.append(w)
        for j in range(i, l_len):
            np = prod * primes[j]
            if np <= limit:
                stack.append((j + 1, np, (w * weights[j]) % _MOD))
    return prods, wgts


def _prefix_g_map(
    primes: List[int], weights: List[int], limit: int, x_values: List[int]
) -> Dict[int, int]:
    l_len = len(primes)
    mid = l_len // 2
    p1, w1 = primes[:mid], weights[:mid]
    p2, w2 = primes[mid:], weights[mid:]

    prods1, wgts1 = _gen_products_weights(p1, w1, limit)
    prods2, wgts2 = _gen_products_weights(p2, w2, limit)

    pairs1 = sorted(zip(prods1, wgts1), key=lambda t: t[0])
    prods1_sorted = [p for p, _ in pairs1]
    pref1 = [0] * len(pairs1)
    s = 0
    for i, (_, w) in enumerate(pairs1):
        s = (s + w) % _MOD
        pref1[i] = s

    pairs2 = sorted(zip(prods2, wgts2), key=lambda t: t[0])
    prods2_sorted = [p for p, _ in pairs2]
    wgts2_sorted = [w for _, w in pairs2]

    cache: Dict[int, int] = {}
    out: Dict[int, int] = {}

    for x in x_values:
        total = 0
        for pb, wb in zip(prods2_sorted, wgts2_sorted):
            u = x // pb
            if u not in cache:
                pos = bisect.bisect_right(prods1_sorted, u)
                cache[u] = pref1[pos - 1] if pos else 0
            total = (total + wb * cache[u]) % _MOD
        out[x] = total
    return out


def solve(m_val: int = 200, n_val: int = 10**12) -> int:
    """Compute D(m_val!, n_val) modulo 1000000007 using Dirichlet convolution and meet-in-the-middle prefix sums."""
    primes = _primes_upto(m_val)

    a_const = 1
    c_const = 1
    inv2 = pow(2, _MOD - 2, _MOD)

    weights: List[int] = []
    for p in primes:
        a = _v_factorial(m_val, p)
        a_const = (a_const * (a + 1)) % _MOD
        c_const = (c_const * (a + 2)) % _MOD
        weights.append((-a * pow(a + 2, _MOD - 2, _MOD)) % _MOD)

    c_const = (c_const * pow(inv2, len(primes), _MOD)) % _MOD
    k_const = (a_const * c_const) % _MOD

    b_limit = int(math.isqrt(n_val))
    pref_small = _tau_prefix_summatory(b_limit)
    cache_t: Dict[int, int] = {}

    y = n_val if n_val <= 1_000_000_000 else 1_000_000_000

    sums: Dict[int, int] = defaultdict(int)
    stack = [(0, 1, 1)]
    l_len = len(primes)

    while stack:
        i, prod, wg = stack.pop()
        t = n_val // prod
        sums[t] = (sums[t] + wg) % _MOD
        for j in range(i, l_len):
            np = prod * primes[j]
            if np <= y:
                stack.append((j + 1, np, (wg * weights[j]) % _MOD))

    h_sum = 0
    for t, ws in sums.items():
        tt = _t_summatory(t, pref_small, b_limit, cache_t) % _MOD
        h_sum = (h_sum + ws * tt) % _MOD

    if y < n_val:
        tmax = n_val // y
        xset = {y}
        for k in range(1, tmax + 2):
            xset.add(n_val // k)
        x_values = sorted(xset)
        g_map = _prefix_g_map(primes, weights, n_val, x_values)

        for t in range(1, tmax + 1):
            r_val = n_val // t
            lb = max(y, n_val // (t + 1))
            interval = (g_map[r_val] - g_map[lb]) % _MOD
            tt = _t_summatory(t, pref_small, b_limit, cache_t) % _MOD
            h_sum = (h_sum + interval * tt) % _MOD

    return (k_const * h_sum) % _MOD


if __name__ == "__main__":
    print(solve())
