"""Project Euler Problem 489: Common Factors Between Two Sequences.

Find H(18, 1900), where H(m, n) = sum_{1<=a<=m, 1<=b<=n} G(a, b),
and G(a, b) is the smallest non-negative integer n maximizing gcd(n^3 + b, (n + a)^3 + b).
"""

from math import isqrt
from typing import Dict, List, Optional, Tuple


def _sieve(limit: int) -> List[int]:
    if limit < 2:
        return []
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if is_prime[p]:
            step = p
            start = p * p
            is_prime[start : limit + 1 : step] = b"\x00" * (
                ((limit - start) // step) + 1
            )
    return [i for i, v in enumerate(is_prime) if v]


_PRIMES = _sieve(12000)


def _tonelli_shanks(n: int, p: int) -> Optional[int]:
    n %= p
    if n == 0:
        return 0
    if p == 2:
        return n
    if pow(n, (p - 1) // 2, p) != 1:
        return None
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)

    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1

    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)

    while t != 1:
        i = 1
        t2i = (t * t) % p
        while i < m and t2i != 1:
            t2i = (t2i * t2i) % p
            i += 1
        if i == m:
            return None
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r


def _factorize_upto_1e8(n: int) -> Dict[int, int]:
    res: Dict[int, int] = {}
    x = n
    for p in _PRIMES:
        if p * p > x:
            break
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            res[p] = e
    if x > 1:
        res[x] = res.get(x, 0) + 1
    return res


def _initial_solutions_mod_p(a: int, b: int, p: int) -> List[int]:
    b_mod = b % p
    if a % p == 0:
        sols = []
        for n in range(p):
            if (pow(n, 3, p) + b_mod) % p == 0 and (
                pow(n + a, 3, p) + b_mod
            ) % p == 0:
                sols.append(n)
        return sols

    if p == 3:
        return []

    if p == 2:
        return [
            n
            for n in range(2)
            if ((n * n * n + b) % 2 == 0 and (((n + a) ** 3) + b) % 2 == 0)
        ]

    a_mod = a % p
    disc = (-3 * a_mod * a_mod) % p
    sqrt_disc = _tonelli_shanks(disc, p)
    if sqrt_disc is None:
        return []

    inv6 = pow(6 % p, -1, p)
    t = (-3 * a_mod) % p

    n1 = (t + sqrt_disc) * inv6 % p
    n2 = (t - sqrt_disc) * inv6 % p

    sols = []
    for n in {n1, n2}:
        if (pow(n, 3, p) + b_mod) % p == 0 and (
            pow(n + a, 3, p) + b_mod
        ) % p == 0:
            sols.append(n)
    sols.sort()
    return sols


def _linear_solutions_mod_prime(a_coeff: int, b_const: int, p: int) -> List[int]:
    a_coeff %= p
    b_const %= p
    if a_coeff == 0:
        return list(range(p)) if b_const == 0 else []
    return [(b_const * pow(a_coeff, -1, p)) % p]


def _solutions_for_prime_power(
    a: int, b: int, p: int, e_max: int
) -> Tuple[int, List[int]]:
    if e_max <= 0:
        return 0, []

    sols = _initial_solutions_mod_p(a, b, p)
    if not sols:
        return 0, []

    mod = p
    e = 1

    while e < e_max:
        mod2 = mod * p
        new_sols = set()

        for r in sols:
            v1 = (pow(r, 3, mod2) + b) % mod2
            v2 = (pow(r + a, 3, mod2) + b) % mod2
            if v1 % mod != 0 or v2 % mod != 0:
                continue

            c1 = (v1 // mod) % p
            c2 = (v2 // mod) % p

            r_mod_p = r % p
            s_mod_p = (r + a) % p

            a1 = (3 * r_mod_p * r_mod_p) % p
            a2 = (3 * s_mod_p * s_mod_p) % p
            b1 = (-c1) % p
            b2 = (-c2) % p

            t1 = _linear_solutions_mod_prime(a1, b1, p)
            if not t1:
                continue
            t2 = _linear_solutions_mod_prime(a2, b2, p)
            if not t2:
                continue

            if len(t1) == p and len(t2) == p:
                ts = range(p)
            elif len(t1) == p:
                ts = t2
            elif len(t2) == p:
                ts = t1
            else:
                ts = t1 if t1[0] == t2[0] else []

            for t in ts:
                new_sols.add(r + t * mod)

        if not new_sols:
            break

        sols = sorted(new_sols)
        mod = mod2
        e += 1

    return e, sols


def _combine_congruences(
    sols1: List[int], mod1: int, sols2: List[int], mod2: int
) -> Tuple[List[int], int]:
    if mod1 == 1:
        return sorted({s % mod2 for s in sols2}), mod2
    if mod2 == 1:
        return sorted({s % mod1 for s in sols1}), mod1

    inv_mod1 = pow(mod1 % mod2, -1, mod2)
    new_mod = mod1 * mod2
    out = set()

    for x in sols1:
        x %= mod1
        for y in sols2:
            y %= mod2
            t = ((y - x) % mod2) * inv_mod1 % mod2
            out.add(x + mod1 * t)

    return sorted(out), new_mod


def _compute_g(
    a: int,
    b: int,
    a6: List[int],
    fac_a: List[Dict[int, int]],
) -> int:
    r_val = a6[a] + 27 * b * b
    fac_r = _factorize_upto_1e8(r_val)

    fac_m: Dict[int, int] = dict(fac_r)
    for p, e in fac_a[a].items():
        fac_m[p] = fac_m.get(p, 0) + 3 * e

    blocks: List[Tuple[int, int, List[int]]] = []
    for p, em in fac_m.items():
        e, sols = _solutions_for_prime_power(a, b, p, em)
        if e > 0:
            blocks.append((p, e, sols))

    if not blocks:
        return 0

    blocks.sort(key=lambda t: t[0])
    sols = [0]
    mod = 1
    for p, e, sols_p in blocks:
        sols, mod = _combine_congruences(sols, mod, sols_p, p**e)

    return min(sols)


def solve(max_a: int = 18, max_b: int = 1900) -> int:
    """Compute H(m, n) using polynomial resultant bounds, Hensel lifting, and CRT."""
    a6 = [0] * (max_a + 1)
    fac_a: List[Dict[int, int]] = [dict() for _ in range(max_a + 1)]

    for a in range(1, max_a + 1):
        a6[a] = a**6
        x = a
        f: Dict[int, int] = {}
        for p in _PRIMES:
            if p * p > x:
                break
            if x % p == 0:
                e = 0
                while x % p == 0:
                    x //= p
                    e += 1
                f[p] = e
        if x > 1:
            f[x] = f.get(x, 0) + 1
        fac_a[a] = f

    total = 0
    for a in range(1, max_a + 1):
        for b in range(1, max_b + 1):
            total += _compute_g(a, b, a6, fac_a)

    return total


if __name__ == "__main__":
    print(solve())
