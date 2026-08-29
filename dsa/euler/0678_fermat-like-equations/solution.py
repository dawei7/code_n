"""Project Euler Problem 678: Fermat-like Equations.

Find the number of tuples (a, b, c, e, f) with 0 < a < b, e >= 2, f >= 3, and c^f <= 10^18
such that a^e + b^e = c^f.
"""

from collections import Counter
import math
from typing import Dict, List, Set, Tuple


def _iroot(n: int, k: int) -> int:
    """Floor integer k-th root of n (n>=0, k>=1)."""
    if n < 2:
        return n
    x = int(round(n ** (1.0 / k)))
    while (x + 1) ** k <= n:
        x += 1
    while x**k > n:
        x -= 1
    return x


def _sieve_spf(limit: int) -> List[int]:
    spf = list(range(limit + 1))
    r = int(limit**0.5)
    for i in range(2, r + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def _factorize_small(x: int, spf: List[int]) -> Dict[int, int]:
    fac: Dict[int, int] = {}
    while x > 1:
        p = spf[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        fac[p] = fac.get(p, 0) + cnt
    return fac


def _count_e2(
    mult: Counter, rep: Dict[int, Tuple[int, int]], spf: List[int]
) -> int:
    total = 0
    for n, mn in mult.items():
        c, f = rep[n]
        fac_c = _factorize_small(c, spf)

        prod = 1
        valid = True
        for p, a in fac_c.items():
            exp = a * f
            if p % 4 == 3:
                if exp % 2 != 0:
                    valid = False
                    break
            elif p % 4 == 1:
                prod *= exp + 1

        if not valid:
            continue

        r2 = 4 * prod
        axis = 4 if math.isqrt(n) ** 2 == n else 0
        diag = 4 if (n % 2 == 0 and math.isqrt(n // 2) ** 2 == n // 2) else 0
        ways = (r2 - axis - diag) // 8
        total += ways * mn

    return total


def _count_e3(
    mult: Counter, rep: Dict[int, Tuple[int, int]], spf: List[int]
) -> int:
    def gen_divisors_limited(
        prime_pows: List[Tuple[int, int]], limit: int
    ) -> List[int]:
        divs = [1]
        for p, max_e in prime_pows:
            nxt = []
            for d in divs:
                cur = d
                for _ in range(max_e + 1):
                    if cur <= limit:
                        nxt.append(cur)
                    else:
                        break
                    cur *= p
            divs = nxt
        return divs

    isqrt = math.isqrt
    total = 0

    for n, mn in mult.items():
        r = _iroot(n, 3)
        if r >= 2 and r**3 == n:
            continue

        c, f = rep[n]
        fac_c = _factorize_small(c, spf)
        pp = [(p, a * f) for p, a in fac_c.items()]

        limit = 2 * _iroot(n, 3)
        divs = gen_divisors_limited(pp, limit)
        cnt = 0

        for s in divs:
            q = n // s
            ss = s * s
            diff = ss - q
            if diff <= 0 or diff % 3:
                continue

            dnum = 4 * q - ss
            if dnum <= 0 or dnum % 3:
                continue

            d_val = dnum // 3
            rd = isqrt(d_val)
            if rd * rd != d_val:
                continue

            if (s - rd) & 1:
                continue

            a = (s - rd) // 2
            b = (s + rd) // 2
            if a > 0 and a < b and a * a * a + b * b * b == n:
                cnt += 1

        if cnt:
            total += cnt * mn

    return total


def _count_e4_highpowers(n_limit: int, mult: Counter, has_ge5: Set[int]) -> int:
    total = 0
    for n in has_ge5:
        if n > n_limit:
            continue
        max_b = _iroot(n - 1, 4)
        ways = 0
        for b in range(2, max_b + 1):
            rem = n - b**4
            if rem <= 0:
                break
            a = _iroot(rem, 4)
            if a * a * a * a == rem and 0 < a < b:
                ways += 1
        total += ways * mult[n]
    return total


def _count_e4_cubes_only(n_limit: int, mult: Counter, has_ge5: Set[int]) -> int:
    excluded = set(has_ge5)
    L = _iroot(n_limit - 1, 4) + 1
    if L < 3:
        return 0

    a4 = [i**4 for i in range(L)]
    b4 = a4

    M = 13 * 19
    r4_occ = sorted(set(pow(x, 4, M) for x in range(M)))
    cube_set = set(pow(x, 3, M) for x in range(M))
    cube_bool = [i in cube_set for i in range(M)]

    res_to_bs: Dict[int, List[int]] = {r: [] for r in r4_occ}
    for b in range(2, L):
        res_to_bs[b4[b] % M].append(b)

    present_rbs = [r for r in r4_occ if res_to_bs[r]]
    a_res = [a4[a] % M for a in range(L)]

    cand_b_by_ra: Dict[int, List[int]] = {}
    for ra in r4_occ:
        cand: List[int] = []
        for rb in present_rbs:
            if cube_bool[(ra + rb) % M]:
                cand.extend(res_to_bs[rb])
        cand_b_by_ra[ra] = cand

    total = 0
    for a in range(1, L):
        ra = a_res[a]
        va = a4[a]
        cand = cand_b_by_ra[ra]
        for b in cand:
            if b <= a:
                continue
            s = va + b4[b]
            if s > n_limit:
                continue
            c = _iroot(s, 3)
            if c * c * c == s and s not in excluded:
                total += mult.get(s, 0)

    return total


def _count_e_ge5(n_limit: int, mult: Counter) -> int:
    total = 0
    for e in range(5, 61):
        lim = _iroot(n_limit, e)
        if lim < 2:
            break
        pows = [pow(i, e) for i in range(1, lim + 1)]
        for i in range(lim - 1):
            pi = pows[i]
            for j in range(i + 1, lim):
                s = pi + pows[j]
                if s > n_limit:
                    break
                total += mult.get(s, 0)
    return total


def solve(n: int = 1_000_000_000_000_000_000) -> int:
    """Find the number of (a, b, c, e, f) tuples satisfying a^e + b^e = c^f <= n."""
    mult: Counter = Counter()
    rep: Dict[int, Tuple[int, int]] = {}
    has_ge5: Set[int] = set()

    for f in range(3, 61):
        maxc = _iroot(n, f)
        if maxc < 2:
            break
        for c in range(2, maxc + 1):
            val = pow(c, f)
            mult[val] += 1
            if val not in rep:
                rep[val] = (c, f)
            if f >= 5:
                has_ge5.add(val)

    spf = _sieve_spf(_iroot(n, 3))
    ans = (
        _count_e2(mult, rep, spf)
        + _count_e3(mult, rep, spf)
        + _count_e4_highpowers(n, mult, has_ge5)
        + _count_e4_cubes_only(n, mult, has_ge5)
        + _count_e_ge5(n, mult)
    )
    return ans


if __name__ == "__main__":
    print(solve())
