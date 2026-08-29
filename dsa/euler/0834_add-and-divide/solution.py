"""Project Euler Problem 834: Add and Divide.

Mathematical reduction:
The m-th term of the sequence is:
  a_m = n + sum_{i=1}^m (n + i) = (m + 1)(2n + m) / 2
We require (n + m) | a_m.
Let X = n + m (so m = X - n).
Then 2 * a_m = (X - n + 1)(X + n) = X^2 + X - n(n - 1).
Divisibility condition:
  X | a_m  <=>  2X | (X(X + 1) - n(n - 1))
           <=>  X(X + 1) - n(n - 1) = 2kX
           <=>  n(n - 1) = X(X + 1 - 2k)

Let A = X and B = X + 1 - 2k.
Then A * B = n(n - 1), where A + B = 2X + 1 - 2k is odd.
Thus, A and B must have opposite parities!
Since m = A - n >= 1, we require A >= n + 1 (which means B = n(n - 1)/A < n).
Every pair of divisors (A, B) with A * B = n(n - 1), A > n, and A != B (mod 2)
corresponds to a unique valid m = A - n.

To compute U(N) = sum_{n=3}^N T(n):
- Precompute Smallest Prime Factor (SPF) sieve up to N.
- For each n, factorize n into 2^{v2} * prod p_i^{e_i}.
- Combine the prime factorizations of n and n - 1 (which are coprime).
- To enforce the parity condition, the 2-adic valuation 2^{v2(n) + v2(n-1)} must be
  entirely allocated to either A or B.
- Generate all odd divisors d_odd of n(n - 1), yielding two complementary pairs:
    1) d = d_odd,       A = n(n-1)/d (even)
    2) d = d_odd * 2^v, A = n(n-1)/d (odd)
- Accumulate (A - n) for each d < n.
"""

from __future__ import annotations


def solve(n: int = 1234567) -> int:
    """Compute U(N) = sum_{n=3}^N T(n) in O(N * d(N)) time."""
    # 1. Precompute SPF (smallest prime factor) for 1..N
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i

    def factorize_odd(x: int) -> tuple[int, list[tuple[int, int]]]:
        v2 = 0
        while (x & 1) == 0:
            v2 += 1
            x >>= 1
        factors = []
        while x > 1:
            p = spf[x]
            e = 0
            while x % p == 0:
                e += 1
                x //= p
            factors.append((p, e))
        return v2, factors

    total_u = 0
    prev_v2, prev_factors = 0, []

    for curr_n in range(2, n + 1):
        curr_v2, curr_factors = factorize_odd(curr_n)
        if curr_n >= 3:
            v2 = curr_v2 + prev_v2
            odd_factors = curr_factors + prev_factors
            p_prod = curr_n * (curr_n - 1)
            two_pow = 1 << v2

            # Generate all odd divisors
            divisors = [1]
            for p, e in odd_factors:
                p_pows = [p**k for k in range(1, e + 1)]
                new_divs = list(divisors)
                for d in divisors:
                    for pow_val in p_pows:
                        new_divs.append(d * pow_val)
                divisors = new_divs

            # Sum valid m = A - curr_n for both parity assignments
            tn = 0
            for d_odd in divisors:
                # Case 1: d = d_odd (odd), A is even
                if d_odd < curr_n:
                    tn += p_prod // d_odd - curr_n
                # Case 2: d = d_odd * 2^v (even), A is odd
                d_even = d_odd * two_pow
                if d_even < curr_n:
                    tn += p_prod // d_even - curr_n

            total_u += tn

        prev_v2, prev_factors = curr_v2, curr_factors

    return total_u


if __name__ == "__main__":
    print(solve())
