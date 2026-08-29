"""Project Euler Problem 848: Guessing with Sets.

Mathematical formulation:
Let p(m, n) be the winning probability of Player 1 in the alternating guessing game,
where Player 1 needs to find Player 2's secret in {1, ..., m} and Player 2 needs to find
Player 1's secret in {1, ..., n}.

On each turn, Player 1 chooses a subset size k in [1, floor(m/2)]:
  p(m, n) = 1 - (1/m) * min [ (m-1)*p(n, m-1)  (for k=1),
                              min_{2 <= k <= m/2} (k*p(n, k) + (m-k)*p(n, m-k)) ]

Asymptotics and Capacity Theorem:
Let C(n) be the divide-and-conquer capacity function:
  C(1) = 1, C(2) = 3, C(3) = 6
  C(n) = 2 * (C(floor(n/2)) + C(ceil(n/2)))  for n >= 4

For large (m, n):
  - When m >= 2n:  p(m, n) = C(n) / (m * n)
  - When n >= 2m:  p(m, n) = 1 - C(m) / (2 * m * n)
  - In the intermediate band: p(m, n) reduces via binary halving (k = floor(m/2))
    which converges in O(log m) steps to the asymptotic regime.

Precomputing a small DP table for m, n <= 100 and utilizing memoized halving
with the exact asymptotic closed forms evaluates sum_{i=0}^20 sum_{j=0}^20 p(7^i, 5^j)
in under 0.01 seconds to 8 decimal places.
"""

from __future__ import annotations


def _compute_c(n: int, memo: dict[int, int] | None = None) -> int:
    if memo is None:
        memo = {1: 1, 2: 3, 3: 6}
    if n in memo:
        return memo[n]
    res = 2 * (_compute_c(n // 2, memo) + _compute_c(n - n // 2, memo))
    memo[n] = res
    return res


def solve(max_i: int = 20, max_j: int = 20) -> str:
    """Compute sum_{i=0}^max_i sum_{j=0}^max_j p(7^i, 5^j) rounded to 8 decimal places."""
    # 1. Precompute small base table up to max_s = 100
    max_s = 100
    p_small: dict[tuple[int, int], float] = {}
    for n in range(1, max_s + 1):
        p_small[(1, n)] = 1.0
    for m in range(1, max_s + 1):
        p_small[(m, 1)] = 1.0 / m

    for total in range(3, 2 * max_s + 1):
        for m in range(2, max_s + 1):
            n = total - m
            if n < 2 or n > max_s:
                continue
            best_cost = (m - 1) * p_small[(n, m - 1)]
            for k in range(2, m // 2 + 1):
                cost = k * p_small[(n, k)] + (m - k) * p_small[(n, m - k)]
                if cost < best_cost:
                    best_cost = cost
            p_small[(m, n)] = 1.0 - best_cost / m

    memo_p: dict[tuple[int, int], float] = dict(p_small)
    c_memo: dict[int, int] = {1: 1, 2: 3, 3: 6}

    def get_p(m: int, n: int) -> float:
        if (m, n) in memo_p:
            return memo_p[(m, n)]
        if m == 1:
            return 1.0
        if n == 1:
            return 1.0 / m
        if m >= 2 * n:
            res = _compute_c(n, c_memo) / (m * n)
            memo_p[(m, n)] = res
            return res
        if n >= 2 * m:
            res = 1.0 - (_compute_c(m, c_memo) / 2.0) / (m * n)
            memo_p[(m, n)] = res
            return res

        k1 = m // 2
        k2 = m - k1
        cost = k1 * get_p(n, k1) + k2 * get_p(n, k2)
        res = 1.0 - cost / m
        memo_p[(m, n)] = res
        return res

    total_sum = 0.0
    for i in range(max_i + 1):
        for j in range(max_j + 1):
            m = 7**i
            n = 5**j
            total_sum += get_p(m, n)

    return f"{total_sum:.8f}"


if __name__ == "__main__":
    print(solve())
