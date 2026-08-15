"""Project Euler Problem 580: Squarefree Hilbert Numbers.

Count squarefree Hilbert numbers below 10^16, where a Hilbert number is 4k + 1,
and squarefree means not divisible by h^2 for any Hilbert number h > 1.
"""

from array import array
import math
from typing import Callable, Dict, List, Tuple


def _icbrt(n: int) -> int:
    if n <= 0:
        return 0
    x = int(round(n ** (1.0 / 3.0)))
    while (x + 1) * (x + 1) * (x + 1) <= n:
        x += 1
    while x * x * x > n:
        x -= 1
    return x


def _primes_upto(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    r = int(n**0.5)
    for p in range(2, r + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start : n + 1 : step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def _mobius_sieve(limit: int) -> List[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: List[int] = []
    is_comp = bytearray(limit + 1)
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


class _Mertens:
    __slots__ = ("limit", "mu", "prefix", "cache", "cache_odd")

    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.mu = _mobius_sieve(limit)
        pref = [0] * (limit + 1)
        s = 0
        for i in range(1, limit + 1):
            s += self.mu[i]
            pref[i] = s
        self.prefix = pref
        self.cache: Dict[int, int] = {}
        self.cache_odd: Dict[int, int] = {}

    def get_m(self, n: int) -> int:
        if n <= self.limit:
            return self.prefix[n]
        got = self.cache.get(n)
        if got is not None:
            return got
        res = 1
        l = 2
        while l <= n:
            q = n // l
            r = n // q
            res -= (r - l + 1) * self.get_m(q)
            l = r + 1
        self.cache[n] = res
        return res

    def get_modd(self, n: int) -> int:
        if n <= 0:
            return 0
        got = self.cache_odd.get(n)
        if got is not None:
            return got
        res = 0
        x = n
        while x:
            res += self.get_m(x)
            x //= 2
        self.cache_odd[n] = res
        return res


def _c_mod4_prefix(q: int) -> int:
    r = q & 3
    return 1 if (r == 1 or r == 2) else 0


def _make_sq1_counter(n_max: int) -> Callable[[int], int]:
    mu_limit = max(300_000, _icbrt(n_max) + 10)
    mert = _Mertens(mu_limit)
    mu = mert.mu

    def sq1(x: int) -> int:
        if x <= 0:
            return 0
        d_val = _icbrt(x)
        sqrtx = math.isqrt(x)
        d_val = min(d_val, sqrtx)

        o_count = 0
        t_count = 0

        for d in range(1, d_val + 1, 2):
            md = mu[d]
            if md:
                q = x // (d * d)
                o_count += md * ((q + 1) // 2)
                t_count += md * _c_mod4_prefix(q)

        qmax = x // ((d_val + 1) * (d_val + 1))
        for q in range(1, qmax + 1):
            r = math.isqrt(x // q)
            if r <= d_val:
                continue
            l = math.isqrt(x // (q + 1)) + 1
            if l <= d_val:
                l = d_val + 1
            if l > r:
                continue
            s = mert.get_modd(r) - mert.get_modd(l - 1)
            if s:
                o_count += s * ((q + 1) // 2)
                t_count += s * _c_mod4_prefix(q)

        return (o_count + t_count) // 2

    return sq1


def _sq1_prefix_small(limit: int) -> List[int]:
    if limit <= 0:
        return [0]
    is_sqfree = bytearray(b"\x01") * (limit + 1)
    is_sqfree[0] = 0
    for p in _primes_upto(math.isqrt(limit)):
        sq = p * p
        is_sqfree[sq : limit + 1 : sq] = b"\x00" * (((limit - sq) // sq) + 1)

    pref = [0] * (limit + 1)
    c = 0
    for n in range(1, limit + 1):
        if is_sqfree[n] and (n & 3) == 1:
            c += 1
        pref[n] = c
    return pref


def _segmented_prime_sum(
    n_val: int, p_min: int, sq1_small: List[int]
) -> int:
    limit = math.isqrt(n_val)
    base = _primes_upto(math.isqrt(limit) + 1)

    low = max(p_min + 1, 3)
    if (low & 1) == 0:
        low += 1

    seg_odds = 1 << 20
    total = 0

    while low <= limit:
        high = min(limit + 1, low + 2 * seg_odds)
        size = ((high - low) + 1) // 2
        seg = bytearray(b"\x01") * size

        for p in base[1:]:
            pp = p * p
            if pp >= high:
                break
            start = (low + p - 1) // p * p
            if start < pp:
                start = pp
            if (start & 1) == 0:
                start += p
            idx = (start - low) // 2
            step = p
            seg[idx::step] = b"\x00" * (((size - 1 - idx) // step) + 1)

        for i, flag in enumerate(seg):
            if flag:
                prime = low + 2 * i
                if (prime & 3) == 3 and prime > p_min:
                    q = n_val // (prime * prime)
                    total += sq1_small[q]

        low = high
        if (low & 1) == 0:
            low += 1

    return total


def solve(n: int = 10_000_000_000_000_000) -> int:
    """Count squarefree Hilbert numbers <= n using Du Jiao sieve and segmented prime sum."""
    sq1_func = _make_sq1_counter(n)

    v_val = _icbrt(n)
    qmax = n // ((v_val + 1) * (v_val + 1))
    small_limit = max(v_val, qmax) + 8
    sq1_small = _sq1_prefix_small(small_limit)

    ans = sq1_func(n)
    for p in _primes_upto(v_val):
        if (p & 3) == 3:
            ans += sq1_func(n // (p * p))

    ans += _segmented_prime_sum(n, v_val, sq1_small)
    return ans


if __name__ == "__main__":
    print(solve())
