"""Project Euler Problem 370: Geometric Triangles.

Find the number of integer-sided geometric triangles (a <= b <= c with b^2 = a*c)
with perimeter <= 2.5 * 10^13.
"""

from math import isqrt, sqrt
from typing import List


def solve(limit: int = 25000000000000) -> int:
    """Count geometric triangles with perimeter <= limit using dual squarefree lattice reduction."""
    if limit < 3:
        return 0

    phi = (1.0 + sqrt(5.0)) / 2.0
    denom = sqrt(5.0) + 3.0

    def beatty_sum(alpha: float, n_val: int) -> int:
        """Compute sum_{n=1..n_val} floor(alpha * n) in O(log n_val) steps."""
        if n_val <= 0:
            return 0
        k = int(alpha)
        res = k * n_val * (n_val + 1) // 2
        rem_alpha = alpha - k
        if rem_alpha < 1e-15:
            return res
        m_val = int(rem_alpha * n_val)
        if m_val == 0:
            return res
        return res + n_val * m_val - beatty_sum(1.0 / rem_alpha, m_val)

    def count_lattice_sector(t_val: int) -> int:
        """Count pairs (x, y) with x <= y < phi * x and x^2 + x*y + y^2 <= t_val."""
        if t_val < 3:
            return 0
        n0 = int(sqrt(t_val / denom))
        s1 = beatty_sum(phi, n0) - n0 * (n0 - 1) // 2
        max_x = int(sqrt(t_val / 3.0))
        s2 = 0
        y_curr = int(phi * (n0 + 1))
        for n in range(n0 + 1, max_x + 1):
            while (
                y_curr >= n and n * n + n * y_curr + y_curr * y_curr > t_val
            ):
                y_curr -= 1
            if y_curr < n:
                break
            s2 += y_curr - n + 1
        return s1 + s2

    # For small limits (e.g. sample limit = 10^6), run exact squarefree loop
    if limit <= 10**7:
        max_m = limit // 3
        is_sqfree = [True] * (max_m + 1)
        is_sqfree[0] = False
        for i in range(2, int(sqrt(max_m)) + 1):
            i2 = i * i
            for j in range(i2, max_m + 1, i2):
                is_sqfree[j] = False
        return sum(
            count_lattice_sector(limit // m)
            for m in range(1, max_m + 1)
            if is_sqfree[m]
        )

    # For limit = 2.5 * 10^13, evaluate through Dirichlet hyperbola decomposition:
    # N(L) = sum_{m <= L/3, mu^2(m)=1} H(L // m)
    max_sqrt = 6000000
    mu: List[int] = [0] * (max_sqrt + 1)
    mu[1] = 1
    primes: List[int] = []
    is_prime = [True] * (max_sqrt + 1)
    for i in range(2, max_sqrt + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > max_sqrt:
                break
            is_prime[i * p] = False
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]

    q_prefix = [0] * (max_sqrt + 1)
    for i in range(1, max_sqrt + 1):
        q_prefix[i] = q_prefix[i - 1] + (1 if mu[i] != 0 else 0)

    mu_nonzeros = [
        (k, mu[k]) for k in range(1, max_sqrt + 1) if mu[k] != 0
    ]

    def count_squarefree(x_val: int) -> int:
        if x_val <= max_sqrt:
            return q_prefix[x_val]
        ans = 0
        sq_lim = isqrt(x_val)
        for k, m_sign in mu_nonzeros:
            if k > sq_lim:
                break
            ans += m_sign * (x_val // (k * k))
        return ans

    v_split = min(isqrt(limit // 3), 350000)
    total_count = 0

    # Part 1: Small m <= v_split
    for v in range(1, v_split + 1):
        if mu[v] != 0:
            total_count += count_lattice_sector(limit // v)

    # Part 2: Chunked large m where floor(limit / m) == t
    max_t = limit // (v_split + 1)
    for t in range(1, max_t + 1):
        v_low = limit // (t + 1)
        v_high = min(limit // 3, limit // t)
        v_low = max(v_low, v_split)
        if v_high > v_low:
            delta_q = count_squarefree(v_high) - count_squarefree(v_low)
            if delta_q > 0:
                total_count += delta_q * count_lattice_sector(t)

    return total_count


if __name__ == "__main__":
    print(solve())
