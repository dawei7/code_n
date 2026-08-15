"""Project Euler Problem 397: Triangle on Parabola.

Find F(10^6, 10^9), the number of integer quadruplets (k, a, b, c) such that triangle ABC
on y = x^2/k has at least one 45-degree angle.
"""

from typing import List


def solve(k_max: int = 1_000_000, x_max: int = 1_000_000_000) -> int:
    """Compute F(k_max, x_max) by iterating over chord slopes and factoring 2k^2."""
    # Linear smallest prime factor (SPF) sieve
    spf: List[int] = list(range(k_max + 1))
    primes: List[int] = []
    is_prime = bytearray([1]) * (k_max + 1)

    for i in range(2, k_max + 1):
        if is_prime[i]:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if i * p > k_max:
                break
            is_prime[i * p] = 0
            spf[i * p] = p
            if i % p == 0:
                break

    del primes, is_prime

    two_x = 2 * x_max
    count_a = 0
    count_b = 0
    overlap_ab = 0
    overlap_ac = 0

    for k in range(1, k_max + 1):
        # Generate all divisors of 2*k^2 directly from prime factorization of k
        x = k
        e2 = 0
        while x > 0 and (x & 1) == 0:
            x >>= 1
            e2 += 1
        divs = [1 << i for i in range(2 * e2 + 2)]

        while x > 1:
            p = spf[x]
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            powers = [p**i for i in range(2 * e + 1)]
            divs = [d * pw for d in divs for pw in powers]

        d_val = 2 * k * k
        for d in divs:
            u = d_val // d

            # Angle at leftmost vertex A
            s = k - u
            t = d - k
            if -two_x <= s <= two_x and -two_x <= t <= two_x:
                l_bound = t - x_max
                if l_bound < -x_max:
                    l_bound = -x_max
                u_bound = s + x_max
                if u_bound > x_max:
                    u_bound = x_max
                u2 = (s - 1) // 2
                if u2 < u_bound:
                    u_bound = u2
                if u_bound >= l_bound:
                    count_a += u_bound - l_bound + 1

                # Overlap checking (triangles with multiple 45-degree angles)
                denom = s + k
                if denom and ((k * (s - k)) % denom == 0):
                    q = (k * (s - k)) // denom
                    if -two_x <= q <= two_x and ((s + t - q) & 1) == 0:
                        a = (s + t - q) // 2
                        b = (s + q - t) // 2
                        c = (t + q - s) // 2
                        if -x_max <= a < b < c <= x_max:
                            overlap_ab += 1

                denom2 = k - t
                if denom2 and ((k * (k + t)) % denom2 == 0):
                    q2 = (k * (k + t)) // denom2
                    if -two_x <= q2 <= two_x and ((s + t - q2) & 1) == 0:
                        a = (s + t - q2) // 2
                        b = (s + q2 - t) // 2
                        c = (t + q2 - s) // 2
                        if -x_max <= a < b < c <= x_max:
                            overlap_ac += 1

            # Angle at middle vertex B
            p_val = -(k + u)
            q_val = k + d
            if -two_x <= p_val <= two_x and q_val <= two_x:
                l_bound = p_val - x_max
                if l_bound < -x_max:
                    l_bound = -x_max
                qx = q_val - x_max
                if qx > l_bound:
                    l_bound = qx
                l2 = p_val // 2 + 1
                if l2 > l_bound:
                    l_bound = l2
                u_bound = p_val + x_max
                if u_bound > x_max:
                    u_bound = x_max
                u2 = (q_val - 1) // 2
                if u2 < u_bound:
                    u_bound = u2
                if u_bound >= l_bound:
                    count_b += u_bound - l_bound + 1

    total = 2 * count_a + count_b - 2 * overlap_ab - overlap_ac
    return total


if __name__ == "__main__":
    print(solve())
