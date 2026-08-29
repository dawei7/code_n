"""Project Euler Problem 526: Largest Prime Factors of Consecutive Numbers.

Find h(10^16), where h(n) is the maximum of g(k) = sum_{i=0..8} lpf(k + i)
over all 2 <= k <= n.
"""

from heapq import heapify, heappop, heappush
from typing import List, Optional, Set, Tuple


def _egcd(a: int, b: int) -> Tuple[int, int, int]:
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def _inv_mod(a: int, m: int) -> int:
    g, x, _ = _egcd(a % m, m)
    if g != 1:
        raise ValueError("inverse does not exist")
    return x % m


_MR_SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
_MR_BASES_64 = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in _MR_SMALL_PRIMES:
        if n == p:
            return True
        if n % p == 0:
            return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    for a in _MR_BASES_64:
        a_mod = a % n
        if a_mod == 0:
            continue
        x = pow(a_mod, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def _forbidden_residues(
    polys: List[Tuple[int, int]], p: int
) -> Optional[Set[int]]:
    forb: Set[int] = set()
    for a, b in polys:
        if a % p == 0:
            if b % p == 0:
                return None
            continue
        inva = _inv_mod(a, p)
        forb.add((-b * inva) % p)
    return forb


def _build_wheel_residues(
    polys: List[Tuple[int, int]], wheel_primes: Tuple[int, ...]
) -> Tuple[List[int], int]:
    residues = [0]
    mod = 1
    for p in wheel_primes:
        forb = _forbidden_residues(polys, p)
        if forb is None:
            return [], 0
        allowed = [x for x in range(p) if x not in forb]

        inv = _inv_mod(mod, p)
        new_residues: List[int] = []
        for r in residues:
            r_mod_p = r % p
            for a in allowed:
                k = ((a - r_mod_p) * inv) % p
                new_residues.append(r + mod * k)
        mod *= p
        residues = new_residues

    residues.sort()
    return residues, mod


def _search_best(limit_n: int) -> int:
    classes = [
        (
            311,
            [
                (2520, 311),
                (2520, 313),
                (2520, 317),
                (2520, 319),
                (105, 13),
                (1260, 157),
                (8, 1),
                (630, 79),
                (420, 53),
            ],
        ),
        (
            2201,
            [
                (2520, 2201),
                (2520, 2203),
                (2520, 2207),
                (2520, 2209),
                (420, 367),
                (630, 551),
                (1260, 1103),
                (105, 92),
                (8, 7),
            ],
        ),
    ]

    wheel_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23)
    small_checks = (29, 31, 37, 41, 43, 47)

    heap = []

    for base_r, polys in classes:
        t_max = (limit_n - base_r) // 2520
        residues, m_mod = _build_wheel_residues(polys, wheel_primes)
        if not residues:
            continue
        for rr in residues:
            t0 = t_max - ((t_max - rr) % m_mod)
            if t0 < 0:
                continue
            k0 = 2520 * t0 + base_r
            heap.append((-k0, base_r, t0, rr, m_mod, polys))

    heapify(heap)

    while heap:
        negk, base_r, t, rr, m_mod, polys = heappop(heap)
        t_next = t - m_mod
        if t_next >= 0:
            k_next = 2520 * t_next + base_r
            heappush(heap, (-k_next, base_r, t_next, rr, m_mod, polys))

        vals = [a * t + b for a, b in polys]
        quad = vals[0:4]

        composite = False
        for p in small_checks:
            for x in quad:
                if x != p and x % p == 0:
                    composite = True
                    break
            if composite:
                break
        if composite:
            continue

        for x in quad:
            if not _is_prime(x):
                composite = True
                break
        if composite:
            continue

        for x in vals[4:]:
            if not _is_prime(x):
                composite = True
                break
        if composite:
            continue

        return sum(vals)

    raise RuntimeError("No solution found")


def _lpf_small(n: int) -> int:
    if n <= 1:
        return 1
    best = 1
    d = 2
    m = n
    while d * d <= m:
        if m % d == 0:
            best = d
            while m % d == 0:
                m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        best = max(best, m)
    return best


def solve(limit_n: int = 10**16) -> int:
    """Compute h(n) by wheel-sieve candidate search over maximal 9-prime polynomial blocks."""
    if limit_n <= 1000:
        max_val = 0
        for k in range(2, limit_n + 1):
            cur = sum(_lpf_small(k + i) for i in range(9))
            if cur > max_val:
                max_val = cur
        return max_val

    return _search_best(limit_n)


if __name__ == "__main__":
    print(solve())
