"""Project Euler Problem 755: Not Zeckendorf.

Find S(10^13), where S(n) = sum_{k=0}^n f(k) and f(k) is the number of ways to express k
as the sum of different Fibonacci numbers {1, 2, 3, 5, 8, 13, ...}.
"""

import functools
from typing import Dict, Tuple


def solve(n: int = 10_000_000_000_000) -> int:
    """Compute S(n) using prefix-bounded memoized Fibonacci knapsack divide-and-conquer."""
    fibs = [1, 2]
    while fibs[-1] <= n * 2:
        fibs.append(fibs[-1] + fibs[-2])

    pref = [0]
    for f in fibs:
        pref.append(pref[-1] + f)

    memo: Dict[Tuple[int, int], int] = {}

    def count_subsets(i: int, x: int) -> int:
        if x < 0:
            return 0
        if i == 0:
            return 1
        if x >= pref[i]:
            return 1 << i

        state = (i, x)
        if state in memo:
            return memo[state]

        ans = count_subsets(i - 1, x) + count_subsets(i - 1, x - fibs[i - 1])
        memo[state] = ans
        return ans

    m = 0
    while m < len(fibs) and fibs[m] <= n:
        m += 1
    m = min(len(fibs), m + 2)

    return count_subsets(m, n)


if __name__ == "__main__":
    print(solve())
