"""Project Euler Problem 423: Consecutive Die Throws.

Find S(50_000_000) mod 10^9+7, where S(L) is the sum of C(n) for 1 <= n <= L,
and C(n) is the number of 6-sided die throw sequences of length n with <= pi(n) matches.
"""

from array import array
from math import isqrt

MOD = 1_000_000_007


def _sieve_odd_primes_upto(n: int) -> bytearray:
    size = n // 2 + 1
    s = bytearray(b"\x01") * size
    if size:
        s[0] = 0

    limit = isqrt(n)
    for p in range(3, limit + 1, 2):
        if s[p >> 1]:
            start = (p * p) >> 1
            step = p
            cnt = ((size - start - 1) // step) + 1
            s[start::step] = b"\x00" * cnt
    return s


def solve(l_limit: int = 50_000_000) -> int:
    """Compute S(l_limit) mod MOD using O(1) step transitions for consecutive match distributions."""
    if l_limit <= 0:
        return 0

    odd_prime = _sieve_odd_primes_upto(l_limit)
    pi_l = (1 if l_limit >= 2 else 0) + odd_prime.count(1)
    d_l = l_limit - pi_l

    max_needed = max(d_l, pi_l + 1) + 2
    inv = array("I", [0]) * (max_needed + 1)
    inv[1] = 1
    for i in range(2, max_needed + 1):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

    inv5 = pow(5, MOD - 2, MOD)

    # Base at n=1
    c_val = 6
    b_val = 6
    k_val = 0
    d_val = 1
    s_sum = c_val % MOD

    if l_limit == 1:
        return s_sum

    # Step to n=2 (prime)
    c_val = 36
    b_val = 6
    k_val = 1
    d_val = 1
    s_sum = (s_sum + c_val) % MOD

    if l_limit == 2:
        return s_sum

    n = 2
    while n <= l_limit - 2:
        m = n + 1
        if odd_prime[m >> 1]:
            extra = (b_val * inv5) % MOD
            extra = (extra * (d_val - 1)) % MOD
            extra = (extra * inv[k_val + 1]) % MOD

            c1 = (6 * c_val + 5 * extra) % MOD
            b1 = (b_val + 5 * extra) % MOD
            k1 = k_val + 1
            d1 = d_val
        else:
            c1 = (6 * c_val - b_val) % MOD
            b1 = (b_val * 5) % MOD
            b1 = (b1 * n) % MOD
            b1 = (b1 * inv[d_val]) % MOD
            k1 = k_val
            d1 = d_val + 1

        s_sum = (s_sum + c1) % MOD

        # Step 2: m (odd) -> m+1 (even, composite for m+1 > 2)
        c2 = (6 * c1 - b1) % MOD
        b2 = (b1 * 5) % MOD
        b2 = (b2 * m) % MOD
        b2 = (b2 * inv[d1]) % MOD
        s_sum = (s_sum + c2) % MOD

        c_val, b_val, k_val, d_val = c2, b2, k1, d1 + 1
        n = m + 1

    if n == l_limit - 1:
        m = l_limit
        if (m & 1) == 0:
            c_val = (6 * c_val - b_val) % MOD
            b_val = (b_val * 5) % MOD
            b_val = (b_val * (l_limit - 1)) % MOD
            b_val = (b_val * inv[d_val]) % MOD
        else:
            if odd_prime[m >> 1]:
                extra = (b_val * inv5) % MOD
                extra = (extra * (d_val - 1)) % MOD
                extra = (extra * inv[k_val + 1]) % MOD
                c_val = (6 * c_val + 5 * extra) % MOD
                b_val = (b_val + 5 * extra) % MOD
                k_val += 1
            else:
                c_val = (6 * c_val - b_val) % MOD
                b_val = (b_val * 5) % MOD
                b_val = (b_val * (l_limit - 1)) % MOD
                b_val = (b_val * inv[d_val]) % MOD
                d_val += 1
        s_sum = (s_sum + c_val) % MOD

    return s_sum


if __name__ == "__main__":
    print(solve())
