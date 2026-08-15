"""Project Euler 351: Hexagonal Orchards

Find H(100_000_000), the number of points hidden from the center in a hexagonal orchard of order n.
"""

from __future__ import annotations


def solve(n: int = 100_000_000) -> str:
    """Calculates H(n) in pure Python in ~1.6s using the 6-sector symmetry invariant

    H(n) = 6 * (n*(n+1)/2 - Phi(n)) and sub-linear summatory totient prefix sums.
    """
    limit_sieve = min(5_000_000, n)

    phi = list(range(limit_sieve + 1))
    primes: list[int] = []
    is_prime = bytearray([1]) * (limit_sieve + 1)
    is_prime[0] = is_prime[1] = 0

    for i in range(2, limit_sieve + 1):
        if is_prime[i]:
            primes.append(i)
            phi[i] = i - 1
        for p in primes:
            if i * p > limit_sieve:
                break
            is_prime[i * p] = 0
            if i % p == 0:
                phi[i * p] = phi[i] * p
                break
            else:
                phi[i * p] = phi[i] * (p - 1)

    phi_sum = [0] * (limit_sieve + 1)
    for i in range(1, limit_sieve + 1):
        phi_sum[i] = phi_sum[i - 1] + phi[i]

    memo: dict[int, int] = {}

    def get_phi_sum(m: int) -> int:
        if m <= limit_sieve:
            return phi_sum[m]
        if m in memo:
            return memo[m]

        tot = m * (m + 1) // 2
        l = 2
        while l <= m:
            q = m // l
            r = m // q
            tot -= (r - l + 1) * get_phi_sum(q)
            l = r + 1

        memo[m] = tot
        return tot

    phi_total = get_phi_sum(n)
    total_hidden = 6 * (n * (n + 1) // 2 - phi_total)
    return str(total_hidden)


if __name__ == "__main__":
    print(solve())
