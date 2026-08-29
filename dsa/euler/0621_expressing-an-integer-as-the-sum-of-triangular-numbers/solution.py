"""Project Euler Problem 621: Expressing an Integer as the Sum of Triangular Numbers.

Find G(17526 * 10^9), where G(n) is the number of ways to express n as the sum of three triangular numbers.
"""

import math
import random
from typing import Dict, List, Optional, Tuple

_MR_BASES_64 = (2, 3, 5, 7, 11, 13, 17)


def _isqrt(n: int) -> int:
    return int(math.isqrt(n))


def _is_probable_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    def check(a: int) -> bool:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    for a in _MR_BASES_64:
        if a % n == 0:
            continue
        if not check(a):
            return False
    return True


def _pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if _is_probable_prime(n):
        return n

    while True:
        c = random.randrange(1, n)
        f_poly = lambda x: ((x * x) % n + c) % n
        x = random.randrange(0, n)
        y = x
        d = 1
        while d == 1:
            x = f_poly(x)
            y = f_poly(f_poly(y))
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d


def _factorize(
    n: int, out: Optional[Dict[int, int]] = None
) -> Dict[int, int]:
    if out is None:
        out = {}
    if n == 1:
        return out
    if _is_probable_prime(n):
        out[n] = out.get(n, 0) + 1
        return out
    d = _pollard_rho(n)
    _factorize(d, out)
    _factorize(n // d, out)
    return out


def _legendre_symbol(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    t = pow(a, (p - 1) // 2, p)
    return -1 if t == p - 1 else 1


def _tonelli_shanks(n: int, p: int) -> Optional[int]:
    n %= p
    if n == 0:
        return 0
    if _legendre_symbol(n, p) != 1:
        return None
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)

    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    z = 2
    while _legendre_symbol(z, p) != -1:
        z += 1

    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s

    while t != 1:
        i = 1
        t2 = (t * t) % p
        while i < m and t2 != 1:
            t2 = (t2 * t2) % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i
    return r


def _hensel_lift_root(n: int, p: int, e: int, r: int) -> int:
    pe = p
    r_mod = r % p
    for _ in range(1, e):
        diff = r_mod * r_mod - n
        rhs = (diff // pe) % p
        inv = pow((2 * r_mod) % p, -1, p)
        t = (-rhs * inv) % p
        r_mod = r_mod + t * pe
        pe *= p
    return r_mod % pe


def _roots_mod_prime_power(n: int, p: int, e: int) -> List[int]:
    pe = p**e
    n %= pe

    if n % p == 0:
        if n == 0:
            step = p ** ((e + 1) // 2)
            return list(range(0, pe, step))
        return [0] if e == 1 else []

    r = _tonelli_shanks(n, p)
    if r is None:
        return []
    if e > 1:
        r = _hensel_lift_root(n, p, e, r)
    r2 = (-r) % pe
    if r2 == r:
        return [r]
    return [r, r2]


def _crt_pair(a1: int, m1: int, a2: int, m2: int) -> Tuple[int, int]:
    if m1 == 1:
        return a2 % m2, m2
    if m2 == 1:
        return a1 % m1, m1
    t = ((a2 - a1) % m2) * pow(m1, -1, m2) % m2
    x = a1 + m1 * t
    return x % (m1 * m2), m1 * m2


def _sieve_spf(n: int) -> List[int]:
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:
            step = i
            start = i * i
            for j in range(start, n + 1, step):
                if spf[j] == j:
                    spf[j] = i
    return spf


def _factorize_small(x: int, spf: List[int]) -> List[Tuple[int, int]]:
    fac: List[Tuple[int, int]] = []
    while x > 1:
        p = spf[x]
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        fac.append((p, e))
    return fac


def _class_number(d_val: int) -> int:
    abs_d = -d_val
    amax = _isqrt(abs_d // 3)
    spf = _sieve_spf(amax)
    root_cache: Dict[Tuple[int, int], List[int]] = {}

    def roots_mod_prime_power_cached(p: int, e: int) -> List[int]:
        key = (p, e)
        if key not in root_cache:
            root_cache[key] = _roots_mod_prime_power(d_val, p, e)
        return root_cache[key]

    h = 0
    for a in range(1, amax + 1, 2):
        fac_a = _factorize_small(a, spf)
        bad = False
        for p, e in fac_a:
            if e >= 2 and d_val % p == 0:
                bad = True
                break
        if bad:
            continue

        roots = [0]
        mod = 1
        ok = True
        for p, e in fac_a:
            pe = p**e
            rset = roots_mod_prime_power_cached(p, e)
            if not rset:
                ok = False
                break
            new_roots: List[int] = []
            new_mod = mod * pe
            for r0 in roots:
                for r in rset:
                    x, m = _crt_pair(r0, mod, r, pe)
                    new_roots.append(x)
            roots = new_roots
            mod = new_mod
        if not ok:
            continue

        for r in roots:
            b = a if r == 0 else (r if (r & 1) else (r - a))
            if abs(b) > a:
                continue

            num = b * b - d_val
            den = 4 * a
            if num % den != 0:
                continue
            c = num // den
            if a > c:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            h += 1

    return h


def solve(n: int = 17526 * 10**9) -> int:
    """Compute G(n) = r_3(8n+3)/8 using Gauss's Hurwitz class number formula."""
    big_n = 8 * n + 3
    fac_n = _factorize(big_n)

    n0 = 1
    f_val = 1
    for p, e in fac_n.items():
        if e & 1:
            n0 *= p
        f_val *= p ** (e // 2)

    d_disc = -n0
    h_val = _class_number(d_disc)

    if d_disc == -3:
        w_div2 = 3
    elif d_disc == -4:
        w_div2 = 2
    else:
        w_div2 = 1

    if f_val == 1:
        s_val = 1
    else:
        fac_f = _factorize(f_val)
        primes = list(fac_f.keys())
        exps = [fac_f[p] for p in primes]

        s_val = 0
        for mask in range(1 << len(primes)):
            bits = 0
            jac = 1
            sig = 1
            for i, p in enumerate(primes):
                e = exps[i]
                if (mask >> i) & 1:
                    bits += 1
                    jac *= _legendre_symbol(d_disc, p)
                    e -= 1
                if e < 0:
                    sig = 0
                    break
                sig *= (p ** (e + 1) - 1) // (p - 1)
            if sig == 0:
                continue
            sign = -1 if (bits & 1) else 1
            s_val += sign * jac * sig

    return (3 * h_val * s_val) // w_div2


if __name__ == "__main__":
    print(solve())
