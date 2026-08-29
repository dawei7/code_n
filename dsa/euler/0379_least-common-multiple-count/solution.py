"""Project Euler Problem 379: Least Common Multiple Count.

Find g(10^12) = sum_{n=1..10^12} f(n), where f(n) is the number of pairs (x, y) with
x <= y and lcm(x, y) = n.
"""

from math import isqrt
from typing import Dict, List


def solve(limit: int = 10**12) -> int:
    """Compute g(limit) via 3D Dirichlet hyperbola evaluation of D_3(M)."""
    if limit <= 0:
        return 0

    max_k = isqrt(limit)

    # 1. Linear sieve for Mobius function mu up to sqrt(limit)
    mu: List[int] = [0] * (max_k + 1)
    mu[1] = 1
    primes: List[int] = []
    is_prime = bytearray([1]) * (max_k + 1)

    for i in range(2, max_k + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > max_k:
                break
            is_prime[i * p] = 0
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]

    # 2. 2D Divisor summatory function D_2(X) = sum_{n <= X} d(n)
    def d2(x_val: int) -> int:
        if x_val <= 0:
            return 0
        s_x = isqrt(x_val)
        return 2 * sum(x_val // i for i in range(1, s_x + 1)) - s_x * s_x

    # 3. 3D Divisor summatory function D_3(M) = sum_{a*b*c <= M} 1 via inclusion-exclusion
    def d3(m_val: int) -> int:
        if m_val <= 0:
            return 0
        k_cube = int(m_val ** (1 / 3.0)) + 2
        while k_cube**3 > m_val:
            k_cube -= 1

        t1 = 3 * sum(d2(m_val // a) for a in range(1, k_cube + 1))
        t2 = 0
        for a in range(1, k_cube + 1):
            for b in range(1, k_cube + 1):
                t2 += m_val // (a * b)
        t2 *= 3
        t3 = k_cube**3
        return t1 - t2 + t3

    # 4. Dirichlet convolution sum_{n <= limit} d(n^2) = sum_{k <= sqrt(limit)} mu(k) D_3(limit // k^2)
    sum_d_n2 = 0
    memo: Dict[int, int] = {}

    for k in range(1, max_k + 1):
        if mu[k] != 0:
            m_arg = limit // (k * k)
            if m_arg in memo:
                val = memo[m_arg]
            else:
                val = d3(m_arg)
                if m_arg <= 100000:
                    memo[m_arg] = val
            sum_d_n2 += mu[k] * val

    # g(limit) = (limit + sum_{n <= limit} d(n^2)) // 2
    return (limit + sum_d_n2) // 2


if __name__ == "__main__":
    print(solve())
