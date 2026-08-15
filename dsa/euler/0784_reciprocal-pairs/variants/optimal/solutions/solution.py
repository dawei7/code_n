"""Project Euler Problem 784: Reciprocal Pairs.

Find F(2*10^6), the total sum of p + q for all reciprocal pairs (p, q) with p <= N.
"""

from typing import List, Tuple


def _sieve_spf(limit: int) -> List[int]:
    spf = [0] * (limit + 1)
    spf[1] = 1
    primes: List[int] = []
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            ip = i * p
            if ip > limit or p > spf[i]:
                break
            spf[ip] = p
    return spf


def solve(N: int = 2_000_000) -> int:
    """Compute F(N) by factoring r^2 - 1 = (r-1)(r+1) and generating all valid divisors k <= min(r-1, N-r)."""
    if N <= 2:
        return 0

    spf = _sieve_spf(N + 2)
    total = 0

    for r in range(2, N):
        kmax = N - r
        if kmax > r - 1:
            kmax = r - 1
        if kmax <= 0:
            continue

        n_val = r * r - 1
        base = 2 * r

        if kmax == 1:
            total += base + 1 + n_val
            continue

        a = r - 1
        b = r + 1

        factors: List[Tuple[int, int]] = []

        if r & 1:
            ea = (a & -a).bit_length() - 1
            eb = (b & -b).bit_length() - 1
            e2 = ea + eb
            a >>= ea
            b >>= eb
            if 2 <= kmax:
                factors.append((2, e2))

        x = a
        while x > 1:
            p = spf[x]
            if p > kmax:
                break
            e = 0
            while x > 1 and spf[x] == p:
                e += 1
                x //= p
            factors.append((p, e))

        x = b
        while x > 1:
            p = spf[x]
            if p > kmax:
                break
            e = 0
            while x > 1 and spf[x] == p:
                e += 1
                x //= p
            factors.append((p, e))

        divs = [1]
        for p, e in factors:
            prev = divs
            new_divs: List[int] = []
            new_append = new_divs.append
            pow_p = 1
            for _ in range(e + 1):
                for d in prev:
                    v = d * pow_p
                    if v <= kmax:
                        new_append(v)
                pow_p *= p
                if pow_p > kmax:
                    break
            divs = new_divs

        for k in divs:
            total += base + k + (n_val // k)

    return total


if __name__ == "__main__":
    print(solve())
