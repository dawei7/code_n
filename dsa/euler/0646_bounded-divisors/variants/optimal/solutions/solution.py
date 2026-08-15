"""Project Euler Problem 646: Bounded Divisors.

Find S(70!, 10^20, 10^60) mod 1000000007, where S(n, L, H) = sum_{d | n, L <= d <= H} lambda(d) * d.
"""

from bisect import bisect_right
from math import isqrt
from typing import Dict, List, Optional, Tuple

_MOD = 1_000_000_007


def _sieve_primes(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    r = int(n**0.5)
    for i in range(2, r + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start : n + 1 : step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i in range(n + 1) if sieve[i]]


def _factorial_prime_exponents(n: int) -> Tuple[List[int], Dict[int, int]]:
    primes = _sieve_primes(n)
    exps: Dict[int, int] = {}
    for p in primes:
        e = 0
        m = n
        while m:
            m //= p
            e += m
        exps[p] = e
    return primes, exps


def _choose_store_subset(
    primes: List[int], exps: Dict[int, int], max_store: int
) -> List[int]:
    eplus = [exps[p] + 1 for p in primes]
    total = 1
    for v in eplus:
        total *= v
    target = isqrt(total)

    m = len(primes)
    best_diff = None
    best_mask = 0

    for mask in range(1 << m):
        prod = 1
        for i in range(m):
            if (mask >> i) & 1:
                prod *= eplus[i]
                if prod > max_store:
                    break
        else:
            comp = total // prod
            if prod > comp:
                continue
            diff = abs(prod - target)
            if best_diff is None or diff < best_diff:
                best_diff = diff
                best_mask = mask

    return [primes[i] for i in range(m) if (best_mask >> i) & 1]


def _precompute_powers(
    p: int, e: int, mod: Optional[int]
) -> Tuple[List[int], List[int]]:
    pow_val = [1] * (e + 1)
    pow_coef = [1] * (e + 1)
    if mod is None:
        for k in range(1, e + 1):
            pow_val[k] = pow_val[k - 1] * p
            pow_coef[k] = pow_coef[k - 1] * (-p)
    else:
        negp = (mod - (p % mod)) % mod
        for k in range(1, e + 1):
            pow_val[k] = pow_val[k - 1] * p
            pow_coef[k] = (pow_coef[k - 1] * negp) % mod
    return pow_val, pow_coef


def _gen_divisors_lists(
    primes: List[int], exps: Dict[int, int], mod: Optional[int]
) -> Tuple[List[int], List[int]]:
    vals = [1]
    coefs = [1]
    for p in primes:
        e = exps[p]
        pow_val, pow_coef = _precompute_powers(p, e, mod)
        new_vals = []
        new_coefs = []
        if mod is None:
            for v, c in zip(vals, coefs):
                for pv, pc in zip(pow_val, pow_coef):
                    new_vals.append(v * pv)
                    new_coefs.append(c * pc)
        else:
            for v, c in zip(vals, coefs):
                for pv, pc in zip(pow_val, pow_coef):
                    new_vals.append(v * pv)
                    new_coefs.append((c * pc) % mod)
        vals, coefs = new_vals, new_coefs
    return vals, coefs


def _split_loop_base(
    iter_primes: List[int], exps: Dict[int, int], base_limit: int = 200_000
) -> Tuple[List[int], List[int]]:
    factors = sorted(((exps[p] + 1, p) for p in iter_primes), reverse=True)
    total = 1
    for f, _ in factors:
        total *= f

    base_count = total
    loop: List[int] = []
    base = set(iter_primes)

    for f, p in factors:
        if base_count <= base_limit:
            break
        loop.append(p)
        base.remove(p)
        base_count //= f

    base_primes = sorted(base)
    loop_primes = sorted(loop, key=lambda p: exps[p] + 1, reverse=True)
    return base_primes, loop_primes


def solve(
    n: int = 70,
    l_bound: int = 10**20,
    h_bound: int = 10**60,
    mod: Optional[int] = _MOD,
) -> int:
    """Compute S(n!, L, H) using balanced meet-in-the-middle prime subset convolution."""
    primes, exps = _factorial_prime_exponents(n)
    store_primes = _choose_store_subset(primes, exps, max_store=1_200_000)
    store_set = set(store_primes)
    iter_primes = [p for p in primes if p not in store_set]

    b_vals, b_coefs = _gen_divisors_lists(store_primes, exps, mod)
    pairs = sorted(zip(b_vals, b_coefs), key=lambda t: t[0])
    b_vals = [v for v, _ in pairs]

    prefix = [0]
    s = 0
    if mod is None:
        for _, c in pairs:
            s += c
            prefix.append(s)
    else:
        for _, c in pairs:
            s = (s + c) % mod
            prefix.append(s)

    base_primes, loop_primes = _split_loop_base(
        iter_primes, exps, base_limit=200_000
    )
    base_vals, base_coefs = _gen_divisors_lists(base_primes, exps, mod)
    loop_pow = [_precompute_powers(p, exps[p], mod) for p in loop_primes]

    x_low = l_bound - 1

    def pref(limit: int) -> int:
        return prefix[bisect_right(b_vals, limit)]

    total = 0
    lp = len(loop_pow)

    if mod is None:
        if lp == 0:
            for v, c in zip(base_vals, base_coefs):
                total += c * (pref(h_bound // v) - pref(x_low // v))
        elif lp == 1:
            pv1, pc1 = loop_pow[0]
            for bv, bc in zip(base_vals, base_coefs):
                for p1, c1 in zip(pv1, pc1):
                    v = bv * p1
                    c = bc * c1
                    total += c * (pref(h_bound // v) - pref(x_low // v))
        elif lp == 2:
            pv1, pc1 = loop_pow[0]
            pv2, pc2 = loop_pow[1]
            for bv, bc in zip(base_vals, base_coefs):
                for p1, c1 in zip(pv1, pc1):
                    v1 = bv * p1
                    c1b = bc * c1
                    for p2, c2 in zip(pv2, pc2):
                        v = v1 * p2
                        c = c1b * c2
                        total += c * (pref(h_bound // v) - pref(x_low // v))
        return total

    m_val = mod
    if lp == 0:
        for v, c in zip(base_vals, base_coefs):
            d = pref(h_bound // v) - pref(x_low // v)
            total = (total + c * (d % m_val)) % m_val
    elif lp == 1:
        pv1, pc1 = loop_pow[0]
        for bv, bc in zip(base_vals, base_coefs):
            for p1, c1 in zip(pv1, pc1):
                v = bv * p1
                coef = (bc * c1) % m_val
                d = pref(h_bound // v) - pref(x_low // v)
                total = (total + coef * (d % m_val)) % m_val
    elif lp == 2:
        pv1, pc1 = loop_pow[0]
        pv2, pc2 = loop_pow[1]
        for bv, bc in zip(base_vals, base_coefs):
            for p1, c1 in zip(pv1, pc1):
                v1 = bv * p1
                c1b = (bc * c1) % m_val
                for p2, c2 in zip(pv2, pc2):
                    v = v1 * p2
                    coef = (c1b * c2) % m_val
                    d = pref(h_bound // v) - pref(x_low // v)
                    total = (total + coef * (d % m_val)) % m_val

    return total % m_val


if __name__ == "__main__":
    print(solve())
