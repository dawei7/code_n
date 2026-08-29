"""Project Euler Problem 593: Fleeting Medians.

Find F(10^7, 10^5), where F(n, k) is the sum of medians of all length-k sliding windows
over sequence S2(1..n) with S(k) = p_k^k mod 10007 and S2(k) = S(k) + S(floor(k/10000) + 1).
"""

import math
from typing import List, Tuple

_MOD = 10007
_PHI = _MOD - 1
_MAX_S2 = 2 * (_MOD - 1)
_DOMAIN_SIZE = _MAX_S2 + 1


def _factorize(n: int) -> List[int]:
    factors: List[int] = []
    x = n
    d = 2
    while d * d <= x:
        if x % d == 0:
            factors.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        factors.append(x)
    return factors


def _build_log_exp_tables(mod: int) -> Tuple[List[int], List[int]]:
    phi = mod - 1
    factors = _factorize(phi)
    g = None
    for cand in range(2, mod):
        ok = True
        for q in factors:
            if pow(cand, phi // q, mod) == 1:
                ok = False
                break
        if ok:
            g = cand
            break
    if g is None:
        raise RuntimeError("Failed to find primitive root")

    exp_table = [0] * phi
    log_table = [-1] * mod
    x = 1
    for i in range(phi):
        exp_table[i] = x
        log_table[x] = i
        x = (x * g) % mod
    return log_table, exp_table


_LOG_TABLE, _EXP_TABLE = _build_log_exp_tables(_MOD)


def _pow_mod_fast(a_mod: int, e_mod: int) -> int:
    if a_mod == 0:
        return 0
    return _EXP_TABLE[(_LOG_TABLE[a_mod] * e_mod) % _PHI]


def _nth_prime_upper_bound(n: int) -> int:
    if n < 6:
        return 15
    x = float(n)
    return int(x * (math.log(x) + math.log(math.log(x))) + 10)


def _sieve_primes_upto(limit: int) -> List[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    r = int(math.isqrt(limit))
    for p in range(2, r + 1):
        if sieve[p]:
            start = p * p
            step = p
            sieve[start : limit + 1 : step] = b"\x00" * (
                ((limit - start) // step) + 1
            )
    return [i for i in range(2, limit + 1) if sieve[i]]


def solve(n: int = 10_000_000, k: int = 100_000) -> str:
    """Compute F(n, k) using segmented prime sieve and drifting median pointer on frequency array."""

    counts = [0] * _DOMAIN_SIZE
    window = [0] * k
    filled = 0
    pos = 0

    even = (k & 1) == 0
    r1 = (k // 2) if even else ((k + 1) // 2)

    m1 = 0
    below = 0
    sum2 = 0

    def init_m1() -> None:
        nonlocal m1, below
        cum = 0
        v_idx = 0
        while cum + counts[v_idx] < r1:
            cum += counts[v_idx]
            v_idx += 1
        m1 = v_idx
        below = cum

    def adjust_m1() -> None:
        nonlocal m1, below
        while below >= r1:
            m1 -= 1
            below -= counts[m1]
        while below + counts[m1] < r1:
            below += counts[m1]
            m1 += 1

    def median2() -> int:
        if not even:
            return m1 << 1
        pos_in = r1 - below
        if pos_in < counts[m1]:
            return m1 << 1
        m2 = m1 + 1
        while counts[m2] == 0:
            m2 += 1
        return m1 + m2

    limit = _nth_prime_upper_bound(n)
    root = int(math.isqrt(limit))
    base_primes = _sieve_primes_upto(root)
    base_odds = [p for p in base_primes if p > 2]
    base_sq = [p * p for p in base_odds]

    offsets = [0] * 1002
    e = 1
    t = 1
    next_t = 10000
    idx = 1

    s = 2
    offsets[1] = s
    v = s + s
    window[0] = v
    counts[v] += 1
    filled = 1

    if k == 1:
        init_m1()
        sum2 += median2()
        if n == 1:
            return f"{sum2 // 2}.{5 if (sum2 & 1) else 0}"

    seg_odds = 1 << 20
    low = 3
    while low <= limit:
        high = min(low + 2 * seg_odds, limit + 1)
        seg_len = (high - low) // 2
        seg = bytearray(b"\x01") * seg_len

        for p, sq in zip(base_odds, base_sq):
            if sq >= high:
                break
            start = sq
            if start < low:
                rem = low % p
                start = low if rem == 0 else low + (p - rem)
                if (start & 1) == 0:
                    start += p
            j = (start - low) // 2
            seg[j::p] = b"\x00" * (((seg_len - j - 1) // p) + 1)

        find = seg.find
        i = find(1)
        while i != -1:
            prime = low + 2 * i
            idx += 1
            e += 1
            if e == _PHI:
                e = 0
            if idx == next_t:
                t += 1
                next_t += 10000

            pm = prime % _MOD
            s = _pow_mod_fast(pm, e)
            if idx <= 1001:
                offsets[idx] = s
            v = s + offsets[t]

            if filled < k:
                window[filled] = v
                counts[v] += 1
                filled += 1
                if filled == k:
                    init_m1()
                    sum2 += median2()
                if idx == n:
                    return f"{sum2 // 2}.{5 if (sum2 & 1) else 0}"
            else:
                out = window[pos]
                if out != v:
                    counts[out] -= 1
                    if out < m1:
                        below -= 1
                    window[pos] = v
                    counts[v] += 1
                    if v < m1:
                        below += 1
                    adjust_m1()
                else:
                    window[pos] = v

                pos += 1
                if pos == k:
                    pos = 0

                sum2 += median2()
                if idx == n:
                    return f"{sum2 // 2}.{5 if (sum2 & 1) else 0}"

            i = find(1, i + 1)

        low = high | 1

    return f"{sum2 // 2}.{5 if (sum2 & 1) else 0}"


if __name__ == "__main__":
    print(solve())
