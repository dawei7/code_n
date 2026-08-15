"""Project Euler Problem 388: Distinct Lines.

Find D(10^10), the number of distinct lines from origin to lattice points in [0, N]^3,
represented as the first 9 digits followed by the last 9 digits.
"""

from typing import Dict, List


def solve(limit: int = 10**10) -> str:
    """Compute D(limit) using sub-linear Mertens function evaluation and hyperbola block summation."""
    # Sieve limit K = O(limit^(2/3))
    k_sieve = min(int(limit ** (2.0 / 3.0)) + 1000, 10_000_000)

    mu: List[int] = [0] * (k_sieve + 1)
    mu[1] = 1
    primes: List[int] = []
    is_prime = bytearray([1]) * (k_sieve + 1)

    for i in range(2, k_sieve + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > k_sieve:
                break
            is_prime[i * p] = 0
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]

    # Precompute small prefix sums of mu
    m_small: List[int] = [0] * (k_sieve + 1)
    running_sum = 0
    for i in range(1, k_sieve + 1):
        running_sum += mu[i]
        m_small[i] = running_sum

    del primes, is_prime

    # Sub-linear Mertens evaluation M(x)
    memo_m: Dict[int, int] = {}

    def mertens(x_val: int) -> int:
        if x_val <= k_sieve:
            return m_small[x_val]
        if x_val in memo_m:
            return memo_m[x_val]

        # M(x) = 1 - sum_{d=2..x} M(floor(x / d))
        res = 1
        l_idx = 2
        while l_idx <= x_val:
            v = x_val // l_idx
            r_idx = x_val // v
            res -= (r_idx - l_idx + 1) * mertens(v)
            l_idx = r_idx + 1

        memo_m[x_val] = res
        return res

    # Block partitioning over floor(limit / k)
    total_d = 0
    l_bound = 1
    while l_bound <= limit:
        m_val = limit // l_bound
        r_bound = limit // m_val

        mu_interval = mertens(r_bound) - mertens(l_bound - 1)
        term = (m_val + 1) ** 3 - 1
        total_d += mu_interval * term

        l_bound = r_bound + 1

    str_ans = str(total_d)
    return str_ans[:9] + str_ans[-9:]


if __name__ == "__main__":
    print(solve())
