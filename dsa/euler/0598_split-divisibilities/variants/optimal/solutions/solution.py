"""Project Euler Problem 598: Split Divisibilities.

Find C(100!), where C(n) is the number of pairs (a, b) with a*b = n, a <= b,
such that d(a) = d(b).
"""

from typing import Dict, List, Tuple


def _primes_upto(n: int) -> List[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    p = 2
    while p * p <= n:
        if sieve[p]:
            step = p
            start = p * p
            sieve[start : n + 1 : step] = b"\x00" * (
                ((n - start) // step) + 1
            )
        p += 1
    return [i for i in range(2, n + 1) if sieve[i]]


def _factorial_prime_exponents(n: int) -> Dict[int, int]:
    exps: Dict[int, int] = {}
    for p in _primes_upto(n):
        e = 0
        m = n
        while m:
            m //= p
            e += m
        exps[p] = e
    return exps


def _build_spf(limit: int) -> List[int]:
    spf = list(range(limit + 1))
    spf[0] = 0
    if limit >= 1:
        spf[1] = 1
    for i in range(2, int(limit**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def _factor_exponents(n: int, spf: List[int]) -> Dict[int, int]:
    out: Dict[int, int] = {}
    while n > 1:
        p = spf[n]
        c = 0
        while n % p == 0:
            n //= p
            c += 1
        out[p] = out.get(p, 0) + c
    return out


def _precompute_vectors(
    limit: int, primes_low: List[int], primes_high: List[int]
) -> Tuple[List[Tuple[int, ...]], List[Tuple[int, ...]], List[bool]]:
    spf = _build_spf(limit)
    vec_low = [(0,) * len(primes_low) for _ in range(limit + 1)]
    vec_high = [(0,) * len(primes_high) for _ in range(limit + 1)]
    has_big = [False] * (limit + 1)

    idx_low = {p: i for i, p in enumerate(primes_low)}
    idx_high = {p: i for i, p in enumerate(primes_high)}

    for n in range(2, limit + 1):
        f = _factor_exponents(n, spf)
        low = [0] * len(primes_low)
        high = [0] * len(primes_high)
        big = False
        for p, e in f.items():
            if p in idx_low:
                low[idx_low[p]] = e
            if p in idx_high:
                high[idx_high[p]] = e
            if p > 47:
                big = True
        vec_low[n] = tuple(low)
        vec_high[n] = tuple(high)
        has_big[n] = big

    return vec_low, vec_high, has_big


def _vec_sub(a: Tuple[int, ...], b: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(x - y for x, y in zip(a, b))


def _vec_add(a: Tuple[int, ...], b: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(x + y for x, y in zip(a, b))


def _convolve_2d(
    dist: Dict[Tuple[int, int], int], deltas: List[Tuple[int, int]]
) -> Dict[Tuple[int, int], int]:
    out: Dict[Tuple[int, int], int] = {}
    for (a_val, b_val), c in dist.items():
        for da, db in deltas:
            k = (a_val + da, b_val + db)
            out[k] = out.get(k, 0) + c
    return out


def solve(n_val: int = 100) -> int:
    """Compute C(n_val!) using prime ratio exponent difference DP and meet-in-the-middle convolution."""
    primes_low = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    primes_high = [29, 31, 37, 41, 43, 47]

    vec_low, vec_high, has_big = _precompute_vectors(
        99, primes_low, primes_high
    )

    primes_fact = _factorial_prime_exponents(n_val)
    big_primes = [5, 7, 11, 13, 17, 19, 23]
    big_es = [primes_fact[p] for p in big_primes]

    options_by_e: Dict[int, List[Tuple[int, int, Tuple[int, ...]]]] = {}
    for e in set(big_es):
        opts = []
        for x in range(e + 1):
            u = x + 1
            v = e - x + 1
            diff = _vec_sub(vec_low[u], vec_low[v])
            d2, d3 = diff[0], diff[1]
            r_tup = diff[2:]
            opts.append((d2, d3, r_tup))
        options_by_e[e] = opts

    m_dist: Dict[Tuple[int, ...], Dict[Tuple[int, int], int]] = {
        (0,) * 7: {(0, 0): 1}
    }

    for e in big_es:
        opts = options_by_e[e]
        new_m: Dict[Tuple[int, ...], Dict[Tuple[int, int], int]] = {}
        for r0, inner in m_dist.items():
            for (d2_0, d3_0), cnt in inner.items():
                for d2_d, d3_d, rd in opts:
                    r1 = _vec_add(r0, rd)
                    key23 = (d2_0 + d2_d, d3_0 + d3_d)
                    inner1 = new_m.get(r1)
                    if inner1 is None:
                        inner1 = {}
                        new_m[r1] = inner1
                    inner1[key23] = inner1.get(key23, 0) + cnt
        m_dist = new_m

    s_dist: Dict[Tuple[int, int], int] = {(0, 0): 1}
    for _ in range(10):
        s_dist = _convolve_2d(s_dist, [(1, 0), (-1, 0)])
    for _ in range(4):
        s_dist = _convolve_2d(s_dist, [(0, 1), (0, 0), (0, -1)])
    for _ in range(2):
        s_dist = _convolve_2d(s_dist, [(-2, 0), (1, -1), (-1, 1), (2, 0)])

    n_all = 0
    u3_infos = []
    for u3 in range(1, 49 + 1):
        v3 = 50 - u3
        dlow3 = _vec_sub(vec_low[u3], vec_low[v3])
        dhigh3 = _vec_sub(vec_high[u3], vec_high[v3])
        u3_infos.append((dlow3, dhigh3))

    for u2 in range(1, 98 + 1):
        v2 = 99 - u2
        if has_big[u2] or has_big[v2]:
            continue

        dlow2 = _vec_sub(vec_low[u2], vec_low[v2])
        dhigh2 = _vec_sub(vec_high[u2], vec_high[v2])

        for dlow3, dhigh3 in u3_infos:
            if any(x != 0 for x in _vec_add(dhigh2, dhigh3)):
                continue

            dlow = _vec_add(dlow2, dlow3)
            target_r = tuple(-x for x in dlow[2:])
            inner = m_dist.get(target_r)
            if inner is None:
                continue

            t2, t3 = -dlow[0], -dlow[1]
            subtotal = 0
            for (s2, s3), scnt in s_dist.items():
                subtotal += inner.get((t2 - s2, t3 - s3), 0) * scnt
            n_all += subtotal

    return n_all // 2


if __name__ == "__main__":
    print(solve())
