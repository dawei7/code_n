"""Project Euler 319: Bounded Sequences

Find t(10^10) mod 10^9, where t(n) is the number of strictly increasing sequences x_1, ..., x_n
with x_1 = 2 such that (x_i)^j < (x_j + 1)^i for all 1 <= i, j <= n.
"""

from __future__ import annotations


def solve(limit_n: int = 10_000_000_000, mod: int = 1_000_000_000) -> str:
    """Calculates t(limit_n) mod mod using the algebraic reduction to distinct roots in (2, 3),

    Mobius inversion: t(n) = sum_{k=1}^n (3^k - 2^k) * M(floor(n / k)),
    sub-linear Mertens function computation, and geometric block summation.
    """
    # 1. Linear sieve for Mobius function up to precomputation threshold
    sieve_limit = 5_000_000
    mu = [0] * (sieve_limit + 1)
    mu[1] = 1
    for i in range(1, sieve_limit + 1):
        if mu[i]:
            for j in range(2 * i, sieve_limit + 1, i):
                mu[j] -= mu[i]

    m_small = [0] * (sieve_limit + 1)
    for i in range(1, sieve_limit + 1):
        m_small[i] = m_small[i - 1] + mu[i]

    # 2. Sub-linear memoized DP for Mertens function M(x) = 1 - sum_{m=2}^x M(floor(x / m))
    memo: dict[int, int] = {}

    def get_mertens(x: int) -> int:
        if x <= sieve_limit:
            return m_small[x]
        if x in memo:
            return memo[x]
        total = 1
        m = 2
        while m <= x:
            q = x // m
            next_m = x // q
            total -= (next_m - m + 1) * get_mertens(q)
            m = next_m + 1
        memo[x] = total
        return total

    # 3. Geometric series block decomposition over intervals of floor(n / k)
    total_t = 0
    k = 1
    mod2 = 2 * mod

    while k <= limit_n:
        q = limit_n // k
        next_k = limit_n // q

        # sum_{i=k}^{next_k} 3^i = (3^(next_k+1) - 3^k) / 2
        pow3_high = pow(3, next_k + 1, mod2)
        pow3_low = pow(3, k, mod2)
        sum3 = ((pow3_high - pow3_low) % mod2) // 2

        # sum_{i=k}^{next_k} 2^i = 2^(next_k+1) - 2^k
        pow2_high = pow(2, next_k + 1, mod)
        pow2_low = pow(2, k, mod)
        sum2 = (pow2_high - pow2_low) % mod

        geom_sum = (sum3 - sum2) % mod
        m_val = get_mertens(q) % mod

        total_t = (total_t + geom_sum * m_val) % mod
        k = next_k + 1

    return str(total_t)


if __name__ == "__main__":
    print(solve())
