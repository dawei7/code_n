"""Project Euler 283: Integer sided triangles with integral area/perimeter ratio

Find the sum of the perimeters of all integer sided triangles for which the
area/perimeter ratios are positive integers not exceeding 1000.
"""

from __future__ import annotations

import math


def solve(limit_m: int = 1000) -> str:
    """Calculates the sum of perimeters of all integer-sided triangles with area/perimeter ratio

    m <= limit_m.

    With inradius r = 2m and tangent segments u, v, w (where side lengths are (v+w)/2, (u+w)/2, (u+v)/2):
    Setting R = 4m, Heron's formula gives:
        (u*v - R^2)(u*w - R^2) = R^2(R^2 + u^2)
    For each m in [1, limit_m] and u in [1, floor(sqrt(3)*R)]:
    We factorize N = R^2(R^2 + u^2) to find all divisor pairs (d1, d2) with d1 * d2 = N and d1 <= d2,
    yielding valid integer tangent lengths u <= v <= w of matching parity.
    """
    max_val = (4 * limit_m) ** 2 + int(math.sqrt(3) * 4 * limit_m + 1) ** 2 + 1000
    sieve_limit = math.isqrt(max_val) + 10
    is_prime = [True] * (sieve_limit + 1)
    is_prime[0] = is_prime[1] = False
    primes: list[int] = []
    for i in range(2, sieve_limit + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, sieve_limit + 1, i):
                is_prime[j] = False

    small_primes = [p for p in primes if p <= 100]
    large_primes = [p for p in primes if p > 100]

    def fast_factorize(n: int) -> list[tuple[int, int]]:
        factors: list[tuple[int, int]] = []
        for p in small_primes:
            if p * p > n:
                break
            if n % p == 0:
                cnt = 0
                while n % p == 0:
                    cnt += 1
                    n //= p
                factors.append((p, cnt))
        if n > 1:
            for p in large_primes:
                if p * p > n:
                    break
                if n % p == 0:
                    cnt = 0
                    while n % p == 0:
                        cnt += 1
                        n //= p
                    factors.append((p, cnt))
            if n > 1:
                factors.append((n, 1))
        return factors

    r_factors: list[list[tuple[int, int]]] = [[]]
    for m in range(1, limit_m + 1):
        r_val = 4 * m
        f_r = fast_factorize(r_val)
        r_factors.append([(p, 2 * e) for p, e in f_r])

    total_perimeters = 0

    for m in range(1, limit_m + 1):
        r_val = 4 * m
        r2 = r_val * r_val
        u_max = int(math.isqrt(3 * r2))
        f_r2 = r_factors[m]

        for u in range(1, u_max + 1):
            val = r2 + u * u
            f_val = fast_factorize(val)

            f_dict: dict[int, int] = {}
            for p, e in f_r2:
                f_dict[p] = e
            for p, e in f_val:
                f_dict[p] = f_dict.get(p, 0) + e

            divs = [1]
            for p, e in f_dict.items():
                cur = 1
                base_divs = list(divs)
                divs = []
                for _ in range(e + 1):
                    for d in base_divs:
                        divs.append(d * cur)
                    cur *= p

            n_val = r2 * val
            for d1 in divs:
                d2 = n_val // d1
                if d1 > d2:
                    continue
                if (r2 + d1) % u == 0:
                    v = (r2 + d1) // u
                    if v >= u:
                        if (r2 + d2) % u == 0:
                            w = (r2 + d2) // u
                            if (u % 2) == (v % 2) == (w % 2):
                                total_perimeters += u + v + w

    return str(total_perimeters)


if __name__ == "__main__":
    print(solve())
