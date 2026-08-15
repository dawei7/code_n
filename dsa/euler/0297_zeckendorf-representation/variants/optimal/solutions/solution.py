"""Project Euler 297: Zeckendorf Representation

Find sum_{n=1}^{10^17 - 1} z(n), where z(n) is the number of terms in the Zeckendorf representation of n.
"""

from __future__ import annotations

import bisect


def solve(limit_n: int = 10**17) -> str:
    """Calculates sum_{n=1}^{limit_n - 1} z(n) in O(log(limit_n)) time using Fibonacci prefix recurrence.

    Let F_1 = 1, F_2 = 2, F_3 = 3, F_4 = 5, ...
    For a full Fibonacci block [0, F_k):
      Z(k) = sum_{n=0}^{F_k - 1} z(n) = Z(k-1) + F_{k-2} + Z(k-2)

    For any general integer N, let F_k be the largest Fibonacci number <= N:
      S(N) = Z(k) + (N - F_k) + S(N - F_k)
    """
    fibs: list[int] = [1, 2]
    while fibs[-1] < limit_n * 2:
        fibs.append(fibs[-1] + fibs[-2])

    z_full: list[int] = [0] * len(fibs)
    z_full[0] = 0  # [0, 1): z(0) = 0
    z_full[1] = 1  # [0, 2): z(0) = 0, z(1) = 1 -> sum = 1

    for i in range(2, len(fibs)):
        z_full[i] = z_full[i - 1] + fibs[i - 2] + z_full[i - 2]

    memo: dict[int, int] = {}

    def get_sum(n: int) -> int:
        if n <= 1:
            return 0
        if n in memo:
            return memo[n]

        idx = bisect.bisect_right(fibs, n) - 1
        f_val = fibs[idx]
        if f_val == n:
            res = z_full[idx]
        else:
            rem = n - f_val
            res = z_full[idx] + rem + get_sum(rem)

        memo[n] = res
        return res

    ans = get_sum(limit_n)
    return str(ans)


if __name__ == "__main__":
    print(solve())
