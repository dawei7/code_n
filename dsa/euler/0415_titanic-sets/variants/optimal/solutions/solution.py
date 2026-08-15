"""Project Euler Problem 415: Titanic Sets.

Find T(10^11) mod 10^8, where T(N) is the number of titanic subsets in an (N+1) x (N+1) grid.
"""

from typing import Dict, List, Set, Tuple

MOD = 100_000_000
PRECOMPUTE = 5_000_000


def _s1(n: int) -> int:
    if n <= 0:
        return 0
    return (n * (n + 1) // 2) % MOD


def _s2(n: int) -> int:
    if n <= 0:
        return 0
    return (n * (n + 1) * (2 * n + 1) // 6) % MOD


def _s3(n: int) -> int:
    if n <= 0:
        return 0
    t = n * (n + 1) // 2
    return (t * t) % MOD


def _range_s1(lo: int, hi: int) -> int:
    return (_s1(hi) - _s1(lo - 1)) % MOD


def _range_s2(lo: int, hi: int) -> int:
    return (_s2(hi) - _s2(lo - 1)) % MOD


def _range_s3(lo: int, hi: int) -> int:
    return (_s3(hi) - _s3(lo - 1)) % MOD


def _pref_k_pow2(n: int, pow2_next: int) -> int:
    if n < 0:
        return 0
    return (((n - 1) % MOD) * pow2_next + 2) % MOD


def _pref_k2_pow2(n: int, pow2_next: int) -> int:
    if n < 0:
        return 0
    k = n % MOD
    return ((k * k - 2 * k + 3) % MOD * pow2_next - 6) % MOD


class _TotientSums:
    def __init__(self, max_n: int) -> None:
        limit = min(max_n, PRECOMPUTE)
        if limit < 1:
            limit = 1
        self.limit = limit

        phi = [0] * (limit + 1)
        phi[1] = 1
        primes: List[int] = []
        composite = bytearray(limit + 1)

        for x in range(2, limit + 1):
            if not composite[x]:
                primes.append(x)
                phi[x] = x - 1
            phix = phi[x]
            for p in primes:
                y = x * p
                if y > limit:
                    break
                composite[y] = 1
                if x % p == 0:
                    phi[y] = phix * p
                    break
                phi[y] = phix * (p - 1)

        pref0 = [0] * (limit + 1)
        pref1 = [0] * (limit + 1)
        pref2 = [0] * (limit + 1)
        for x in range(1, limit + 1):
            ph = phi[x] % MOD
            xm = x % MOD
            pref0[x] = (pref0[x - 1] + ph) % MOD
            pref1[x] = (pref1[x - 1] + xm * ph) % MOD
            pref2[x] = (pref2[x - 1] + xm * xm % MOD * ph) % MOD

        self.pref0 = pref0
        self.pref1 = pref1
        self.pref2 = pref2
        self.cache0: Dict[int, int] = {}
        self.cache1: Dict[int, int] = {}
        self.cache2: Dict[int, int] = {}

    def phi(self, n: int) -> int:
        if n <= self.limit:
            return self.pref0[n]
        cached = self.cache0.get(n)
        if cached is not None:
            return cached

        total = _s1(n)
        lo = 2
        while lo <= n:
            q = n // lo
            hi = n // q
            total = (total - ((hi - lo + 1) % MOD) * self.phi(q)) % MOD
            lo = hi + 1

        self.cache0[n] = total
        return total

    def i_phi(self, n: int) -> int:
        if n <= self.limit:
            return self.pref1[n]
        cached = self.cache1.get(n)
        if cached is not None:
            return cached

        total = _s2(n)
        lo = 2
        while lo <= n:
            q = n // lo
            hi = n // q
            total = (total - _range_s1(lo, hi) * self.i_phi(q)) % MOD
            lo = hi + 1

        self.cache1[n] = total
        return total

    def i2_phi(self, n: int) -> int:
        if n <= self.limit:
            return self.pref2[n]
        cached = self.cache2.get(n)
        if cached is not None:
            return cached

        total = _s3(n)
        lo = 2
        while lo <= n:
            q = n // lo
            hi = n // q
            total = (total - _range_s2(lo, hi) * self.i2_phi(q)) % MOD
            lo = hi + 1

        self.cache2[n] = total
        return total


def _direction_stats(
    sums: _TotientSums, m: int
) -> Tuple[int, int, int]:
    if m <= 0:
        return 0, 0, 0
    count = (2 * sums.phi(m) - 1) % MOD
    coord_sum = (3 * sums.i_phi(m) - 1) % MOD
    product_sum = sums.i2_phi(m)
    return count, coord_sum, product_sum


def solve(n_val: int = 100_000_000_000) -> int:
    """Compute T(n_val) mod 10^8 using Sylvester-Gallai collinear line sieving and sublinear totient sums."""
    sums = _TotientSums(n_val)
    side = n_val + 1
    point_count = side * side
    all_subsets = pow(2, point_count, MOD)
    singleton_part = (1 + (point_count % MOD)) % MOD

    if n_val < 2:
        return (all_subsets - singleton_part) % MOD

    blocks: List[Tuple[int, int, int, int]] = []
    needed: Set[int] = set()
    lo = 2
    while lo <= n_val:
        a = n_val // lo
        b = n_val // (lo + 1) if lo < n_val else 0
        hi_a = n_val // a
        hi_b = n_val // b - 1 if b else n_val
        hi = min(hi_a, hi_b)
        blocks.append((lo, hi, a, b))
        needed.add(a)
        if b:
            needed.add(b)
        lo = hi + 1

    stats = {m: _direction_stats(sums, m) for m in needed}
    side_mod = side % MOD
    side2_mod = side_mod * side_mod % MOD

    collinear = 0
    for lo, hi, m1, m2 in blocks:
        c1, xy1, pr1 = stats[m1]
        c2, xy2, pr2 = stats[m2] if m2 else (0, 0, 0)

        q2 = (pr1 - pr2) % MOD
        q1 = (side_mod * (xy2 - xy1) - 2 * pr2) % MOD
        q0 = (side2_mod * (c1 - c2) + side_mod * xy2 - pr2) % MOD

        p2 = 2 * q2 % MOD
        p1 = 2 * q1 % MOD
        p0 = (2 * q0 + 2 * side_mod) % MOD

        pow_lo = pow(2, lo, MOD)
        pow_after_hi = pow(2, hi + 1, MOD)
        e0 = (pow_after_hi - pow_lo) % MOD
        e1 = (
            _pref_k_pow2(hi, pow_after_hi) - _pref_k_pow2(lo - 1, pow_lo)
        ) % MOD
        e2 = (
            _pref_k2_pow2(hi, pow_after_hi) - _pref_k2_pow2(lo - 1, pow_lo)
        ) % MOD

        poly_exp = (p2 * e2 + p1 * e1 + p0 * e0) % MOD

        r1 = _range_s1(lo, hi)
        r2 = _range_s2(lo, hi)
        r3 = _range_s3(lo, hi)
        length = (hi - lo + 1) % MOD
        poly_plain = (
            p2 * ((r3 + r2) % MOD)
            + p1 * ((r2 + r1) % MOD)
            + p0 * ((r1 + length) % MOD)
        ) % MOD

        collinear = (collinear + poly_exp - poly_plain) % MOD

    ans = (all_subsets - singleton_part - collinear) % MOD
    return ans


if __name__ == "__main__":
    print(solve())
