"""Project Euler Problem 512: Sums of Totients of Powers.

Find g(5 * 10^8), where g(n) = sum_{i=1..n} f(i) and f(n) = (sum_{i=1..n} phi(n^i)) mod (n + 1).
"""

from typing import Dict, List


def solve(n: int = 5 * 10**8) -> int:
    """Compute g(n) using odd totient identity and sublinear Du Sieve for totient summatory function."""
    m_limit = max(1000, int(n ** (2 / 3)))
    if m_limit > n:
        m_limit = n

    phi: List[int] = list(range(m_limit + 1))
    for i in range(2, m_limit + 1):
        if phi[i] == i:
            for j in range(i, m_limit + 1, i):
                phi[j] -= phi[j] // i

    s_small: List[int] = [0] * (m_limit + 1)
    for i in range(1, m_limit + 1):
        s_small[i] = s_small[i - 1] + phi[i]

    memo: Dict[int, int] = {}

    def s_totient(x: int) -> int:
        if x <= m_limit:
            return s_small[x]
        if x in memo:
            return memo[x]

        total = x * (x + 1) // 2
        left = 2
        while left <= x:
            q = x // left
            right = x // q
            total -= (right - left + 1) * s_totient(q)
            left = right + 1

        memo[x] = total
        return total

    ans = s_totient(n)
    temp = n // 2
    while temp > 0:
        ans -= s_totient(temp)
        temp //= 2

    return ans


if __name__ == "__main__":
    print(solve())
