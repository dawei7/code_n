"""Project Euler Problem 362: Squarefree Factors.

Find S(10^10) where S(n) = sum_{k=2..n} Fsf(k), and Fsf(k) is the number of ways k can be factored
into one or more squarefree factors larger than 1.
"""

from math import isqrt


def solve(n: int = 10**10) -> int:
    """Find S(10^10) for sum of squarefree factor partition counts."""
    if n < 2:
        return 0

    max_sqrt = isqrt(n)
    mu = [0] * (max_sqrt + 1)
    mu[1] = 1
    primes = []
    is_p = [True] * (max_sqrt + 1)
    for i in range(2, max_sqrt + 1):
        if is_p[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > max_sqrt:
                break
            is_p[i * p] = False
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]

    # Precomputed squarefree count prefix sums up to max_sqrt
    q_pre = [0] * (max_sqrt + 1)
    for i in range(1, max_sqrt + 1):
        q_pre[i] = q_pre[i - 1] + (1 if mu[i] != 0 else 0)

    sqfree = [i for i in range(2, max_sqrt + 1) if mu[i] != 0]
    mu_nonzeros = [(k, mu[k]) for k in range(1, max_sqrt + 1) if mu[k] != 0]

    q_cache = {}

    def q_count(x: int) -> int:
        """Count number of squarefree integers <= x."""
        if x <= max_sqrt:
            return q_pre[x]
        if x in q_cache:
            return q_cache[x]
        ans = 0
        limit = isqrt(x)
        for k, m in mu_nonzeros:
            if k > limit:
                break
            ans += m * (x // (k * k))
        q_cache[x] = ans
        return ans

    def count(limit: int, min_idx: int) -> int:
        min_d = sqfree[min_idx]
        if min_d > limit:
            return 0

        # Single squarefree factor contribution
        ans = q_count(limit) - q_pre[min_d - 1]

        # Multiple factor branch: d_1 * d_2 * ... <= limit
        max_d1 = isqrt(limit)
        if max_d1 < min_d:
            return ans

        for i in range(min_idx, len(sqfree)):
            d = sqfree[i]
            if d > max_d1:
                break
            ans += count(limit // d, i)
        return ans

    return count(n, 0)


if __name__ == "__main__":
    print(solve())
