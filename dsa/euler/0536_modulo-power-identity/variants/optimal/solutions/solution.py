"""Project Euler Problem 536: Modulo Power Identity.

Find S(10^12), where S(n) is the sum of all positive integers m <= n such that
a^(m+4) = a (mod m) for all integers a.
"""

from math import gcd, isqrt
import sys
from typing import List, Optional, Tuple


def _sieve(limit: int) -> Tuple[bytearray, List[int]]:
    if limit < 2:
        return bytearray(limit + 1), []
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0] = is_prime[1] = 0
    if limit >= 4:
        is_prime[4::2] = b"\x00" * (((limit - 4) // 2) + 1)

    r = isqrt(limit)
    for p in range(3, r + 1, 2):
        if is_prime[p]:
            step = p << 1
            start = p * p
            is_prime[start : limit + 1 : step] = b"\x00" * (
                ((limit - start) // step) + 1
            )

    primes = [2]
    primes.extend([p for p in range(3, limit + 1, 2) if is_prime[p]])
    return is_prime, primes


def solve(limit_n: int = 10**12) -> int:
    """Compute S(limit_n) using Korselt-like condition p-1 | m+3 and pruned branch-and-bound DFS."""
    if limit_n < 1:
        return 0

    pmax = isqrt(limit_n + 4) + 5
    is_prime, primes = _sieve(pmax)

    odd_primes = [p for p in primes if p >= 3]
    primes_after3 = [p for p in odd_primes if p != 3]
    primes_mod3_2 = [p for p in primes_after3 if (p % 3) == 2]

    total = 0
    if limit_n >= 2:
        total += 2

    sys.setrecursionlimit(20000)

    def feasible_progression(
        x: int, lam: int, min_q: int
    ) -> Optional[Tuple[int, int, int]]:
        gx = gcd(x, lam)
        if 3 % gx != 0:
            return None
        step = lam // gx
        if step == 1:
            r0 = 0
        else:
            a = x // gx
            try:
                inv = pow(a, -1, step)
            except ValueError:
                return None
            r0 = ((-3 // gx) % step) * inv % step

        q0 = r0
        if q0 < min_q:
            q0 += ((min_q - q0 + step - 1) // step) * step
        return step, r0, q0

    def leaf_count_last_prime(
        x: int,
        lam: int,
        plist: List[int],
        idx: int,
        q_low: int,
        step: int,
        r0: int,
    ) -> None:
        nonlocal total
        if idx >= len(plist):
            return

        if q_low < plist[idx]:
            q_low = plist[idx]

        max_q = min(limit_n // x, pmax)
        if q_low > max_q:
            return

        if step == 1:
            lo, hi = idx, len(plist)
            while lo < hi:
                mid = (lo + hi) >> 1
                if plist[mid] < q_low:
                    lo = mid + 1
                else:
                    hi = mid
            for j in range(lo, len(plist)):
                q = plist[j]
                if q > max_q:
                    break
                if (x + 3) % (q - 1) == 0:
                    total += x * q
            return

        if step <= 2:
            lo, hi = idx, len(plist)
            while lo < hi:
                mid = (lo + hi) >> 1
                if plist[mid] < q_low:
                    lo = mid + 1
                else:
                    hi = mid
            for j in range(lo, len(plist)):
                q = plist[j]
                if q > max_q:
                    break
                if (q - r0) % step != 0:
                    continue
                if (x + 3) % (q - 1) == 0:
                    total += x * q
            return

        q = r0
        if q < q_low:
            q += ((q_low - q + step - 1) // step) * step
        for cand in range(q, max_q + 1, step):
            if is_prime[cand] and (x + 3) % (cand - 1) == 0:
                total += x * cand

    def dfs(x: int, lam: int, plist: List[int], idx: int) -> None:
        nonlocal total
        if (x + 3) % lam == 0:
            total += x

        if idx >= len(plist):
            return

        bound = isqrt(limit_n // x)
        q_low = bound + 1

        prog = feasible_progression(x, lam, plist[idx])
        if prog is None:
            return
        step, r0, q0 = prog
        if x * q0 > limit_n:
            return

        if q_low <= pmax:
            leaf_count_last_prime(x, lam, plist, idx, q_low, step, r0)

        for j in range(idx, len(plist)):
            p = plist[j]
            if p > bound:
                break

            xp = x * p
            pm1 = p - 1
            d = gcd(lam, pm1)
            lam2 = (lam // d) * pm1

            gp = gcd(xp, lam2)
            if gp not in (1, 3):
                continue

            dfs(xp, lam2, plist, j + 1)

    if limit_n >= 3:
        dfs(3, 2, primes_after3, 0)
    dfs(1, 1, primes_mod3_2, 0)

    return total


if __name__ == "__main__":
    print(solve())
