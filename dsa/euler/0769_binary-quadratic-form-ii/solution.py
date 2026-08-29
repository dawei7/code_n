"""Project Euler Problem 769: Binary Quadratic Form II.

Find C(10^14), the total number of primitive representations of z^2 for 0 < z <= N
under the binary quadratic form f(x, y) = x^2 + 5xy + 3y^2.
"""

from array import array
import math
from typing import List, Tuple

_SQRT3 = math.sqrt(3.0)

_INV_MOD13 = [0] * 13
for _a in range(1, 13):
    _INV_MOD13[_a] = pow(_a, -1, 13)


def _build_spf_linear(n: int) -> array:
    spf = array("I", [0]) * (n + 1)
    primes: List[int] = []
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        si = spf[i]
        for p in primes:
            v = i * p
            if v > n:
                break
            spf[v] = p
            if p == si:
                break
    return spf


def _distinct_prime_factors(n: int, spf: array) -> List[int]:
    res: List[int] = []
    tmp = n
    while tmp > 1:
        p = spf[tmp]
        res.append(p)
        while tmp % p == 0:
            tmp //= p
    return res


def _count_coprime_interval_with_divs(
    n: int, L: int, R: int, spf: array
) -> Tuple[int, List[int], List[int]]:
    primes = _distinct_prime_factors(n, spf)
    ds = [1]
    mus = [1]
    for pr in primes:
        m = len(ds)
        for i in range(m):
            ds.append(ds[i] * pr)
            mus.append(-mus[i])

    Lm = L - 1
    total = 0
    for d, mu in zip(ds, mus):
        total += mu * (R // d - Lm // d)
    return total, ds, mus


def _count_congruence_in_interval(L: int, R: int, mod: int, rem: int) -> int:
    if rem < L:
        rem += ((L - rem + mod - 1) // mod) * mod
    if rem > R:
        return 0
    return 1 + (R - rem) // mod


def _count_coprime_with_mod13_congruence(
    ds: List[int],
    mus: List[int],
    L: int,
    R: int,
    rem13: int,
) -> int:
    total = 0
    for d, mu in zip(ds, mus):
        inv = _INV_MOD13[d % 13]
        m0 = (rem13 * inv) % 13
        rem = d * m0
        mod = 13 * d
        total += mu * _count_congruence_in_interval(L, R, mod, rem)
    return total


def _max_abs_p_for_negative_branch(N: int) -> int:
    hi = int(math.isqrt(N)) + 2
    lo = 0
    while lo + 1 < hi:
        a = (lo + hi) // 2
        if a == 0:
            lo = a
            continue

        qmin = int(_SQRT3 * a) + 1
        thr = 3 * a * a
        while qmin * qmin <= thr:
            qmin += 1

        qmax = (5 * a - 1) // 2
        if qmin > qmax:
            ok = False
        else:
            z = -(qmin * qmin - 5 * a * qmin + 3 * a * a)
            ok = z <= N

        if ok:
            lo = a
        else:
            hi = a
    return lo


def solve(N: int = 100_000_000_000_000) -> int:
    """Compute C(N) using parameterization of binary quadratic form and Mobius interval sieving."""
    fourN = 4 * N
    isqrt = math.isqrt

    maxp = max(int(isqrt(N // 3)), _max_abs_p_for_negative_branch(N))
    spf = _build_spf_linear(maxp)

    total = 0

    # Branch 1: p > 0, q > sqrt(3)*p, z = q^2 + 5pq + 3p^2
    pmax = int(isqrt(N // 3))
    for p in range(1, pmax + 1):
        qmin = int(_SQRT3 * p) + 1
        thr = 3 * p * p
        while qmin * qmin <= thr:
            qmin += 1

        disc = 13 * p * p + fourN
        qmax = (isqrt(disc) - 5 * p) // 2
        if qmax < qmin:
            continue

        pp3 = 3 * p * p
        while qmax >= qmin and (qmax * qmax + 5 * p * qmax + pp3) > N:
            qmax -= 1
        if qmax < qmin:
            continue

        cnt, ds, mus = _count_coprime_interval_with_divs(p, qmin, qmax, spf)

        if p % 13 != 0:
            bad = _count_coprime_with_mod13_congruence(ds, mus, qmin, qmax, (4 * p) % 13)
            cnt -= bad

        total += cnt

    # Branch 2: p = -a < 0, sqrt(3)*a < q < 2.5a, z = -(q^2 - 5aq + 3a^2)
    amax = _max_abs_p_for_negative_branch(N)
    threshold = int(isqrt(fourN // 13))

    for a in range(1, amax + 1):
        qmin = int(_SQRT3 * a) + 1
        thr = 3 * a * a
        while qmin * qmin <= thr:
            qmin += 1

        qmax = (5 * a - 1) // 2
        if qmax < qmin:
            continue

        if a > threshold:
            disc = 13 * a * a - fourN
            s = isqrt(disc)
            lim = (5 * a - s) // 2
            if lim < qmax:
                qmax = lim

        while qmax >= qmin and (-(qmax * qmax - 5 * a * qmax + 3 * a * a)) > N:
            qmax -= 1
        if qmax < qmin:
            continue

        cnt, ds, mus = _count_coprime_interval_with_divs(a, qmin, qmax, spf)

        if a % 13 != 0:
            bad = _count_coprime_with_mod13_congruence(
                ds, mus, qmin, qmax, (-4 * a) % 13
            )
            cnt -= bad

        total += cnt

    return total


if __name__ == "__main__":
    print(solve())
