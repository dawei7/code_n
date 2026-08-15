"""Project Euler Problem 735: Divisors of 2n^2.

Find F(10^12), where F(N) = sum_{n=1}^N f(n) and f(n) is the number of divisors of 2n^2
that are no greater than n.
"""

from array import array
from math import isqrt
from typing import Dict


def _icbrt(n: int) -> int:
    if n <= 0:
        return 0
    x = int(round(n ** (1.0 / 3.0)))
    while (x + 1) * (x + 1) * (x + 1) <= n:
        x += 1
    while x * x * x > n:
        x -= 1
    return x


def _mobius_sieve(n: int) -> array:
    mu = array("i", [0]) * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    is_comp = bytearray(n + 1)

    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            ip = i * p
            if ip > n:
                break
            is_comp[ip] = 1
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]
    return mu


def _build_odd_squarefree_prefix(k_val: int) -> array:
    is_sf = bytearray(b"\x01") * (k_val + 1)
    is_sf[0] = 0
    is_sf[0::2] = b"\x00" * ((k_val // 2) + 1)

    r = isqrt(k_val)
    is_prime = bytearray(b"\x01") * (r + 1)
    if r >= 0:
        is_prime[0] = 0
    if r >= 1:
        is_prime[1] = 0
    for i in range(2, isqrt(r) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            is_prime[start : r + 1 : step] = b"\x00" * (
                ((r - start) // step) + 1
            )

    for p in range(3, r + 1, 2):
        if is_prime[p]:
            sq = p * p
            for m in range(sq, k_val + 1, sq):
                is_sf[m] = 0

    pref = array("I", [0]) * (k_val + 1)
    c = 0
    for i in range(1, k_val + 1):
        c += is_sf[i]
        pref[i] = c
    return pref


def solve(n: int = 1_000_000_000_000, k_max: int = 20_000_000) -> int:
    """Compute F(N) using cube-root accelerated Mobius summation and hyperbolic divisor decomposition."""
    if n <= 1000:
        total = 0
        for i in range(1, n + 1):
            m = 2 * i * i
            cnt = sum(1 for d in range(1, i + 1) if m % d == 0)
            total += cnt
        return total

    k_est = _icbrt(n * n)
    k_val = min(k_max, max(10_000, k_est))
    c_small = _build_odd_squarefree_prefix(k_val)

    two_n = 2 * n
    mu_limit = isqrt(two_n)
    mu = _mobius_sieve(mu_limit)

    m_odd = array("i", [0]) * (mu_limit + 1)
    s = 0
    for i in range(1, mu_limit + 1):
        if i & 1:
            s += mu[i]
        m_odd[i] = s

    a_cache: Dict[int, int] = {}

    def a_odd(y: int) -> int:
        if y <= 0:
            return 0
        got = a_cache.get(y)
        if got is not None:
            return got

        r = isqrt(y)
        t_val = _icbrt(y)
        if t_val > r:
            t_val = r

        total = 0
        for k in range(1, t_val + 1, 2):
            total += mu[k] * (y // (k * k))

        if t_val < r:
            upper_v = y // ((t_val + 1) * (t_val + 1))
            for v in range(1, upper_v + 1):
                hi = isqrt(y // v)
                lo = isqrt(y // (v + 1)) + 1
                if lo <= t_val:
                    lo = t_val + 1
                if lo <= hi:
                    total += v * (m_odd[hi] - m_odd[lo - 1])

        a_cache[y] = total
        return total

    c_cache: Dict[int, int] = {}

    def c_odd_squarefree(x: int) -> int:
        if x <= k_val:
            return int(c_small[x])
        got = c_cache.get(x)
        if got is not None:
            return got
        val = a_odd(x) - a_odd(x // 2)
        c_cache[x] = val
        return val

    lim0 = n // k_val
    lim1 = two_n // k_val

    divcnt = array("I", [0]) * (lim0 + 1)
    for i in range(1, lim0 + 1):
        for j in range(i, lim0 + 1, i):
            divcnt[j] += 1

    s0_small = 0
    for p in range(1, lim0 + 1):
        d = int(divcnt[p])
        r = isqrt(p)
        is_sq = 1 if r * r == p else 0
        pairs = (d - is_sq) // 2
        if pairs:
            s0_small += pairs * c_odd_squarefree(n // p)

    s0_large = 0
    q_max = isqrt(n)
    for q in range(1, q_max + 1):
        t = q + 1
        lim = lim0 // q + 1
        if lim > t:
            t = lim
        t_end = n // q
        if t > t_end:
            continue
        while t <= t_end:
            v = n // (q * t)
            t2 = n // (q * v)
            if t2 > t_end:
                t2 = t_end
            s0_large += (t2 - t + 1) * int(c_small[v])
            t = t2 + 1

    coeff_even = array("I", [0]) * (lim1 + 1)
    for q in range(2, lim1 + 1, 2):
        t_end = lim1 // q
        if t_end > q:
            for t in range(q + 1, t_end + 1):
                coeff_even[q * t] += 1

    s1_small = 0
    for p in range(1, lim1 + 1):
        c_val = int(coeff_even[p])
        if c_val:
            s1_small += c_val * c_odd_squarefree(two_n // p)

    s1_large = 0
    q_max2 = isqrt(two_n)
    for q in range(2, q_max2 + 1, 2):
        t = q + 1
        lim = lim1 // q + 1
        if lim > t:
            t = lim
        t_end = two_n // q
        if t > t_end:
            continue
        while t <= t_end:
            v = two_n // (q * t)
            t2 = two_n // (q * v)
            if t2 > t_end:
                t2 = t_end
            s1_large += (t2 - t + 1) * int(c_small[v])
            t = t2 + 1

    ans = n + (s0_small + s0_large) + (s1_small + s1_large)
    return ans


if __name__ == "__main__":
    print(solve())
