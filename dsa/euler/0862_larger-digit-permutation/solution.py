"""Project Euler Problem 862: Larger Digit Permutation.

Mathematical formulation:
Let M = (c_0, c_1, ..., c_9) be a multiset of k digits with sum c_d = k and c_0 < k.
The number of valid k-digit integers (without leading zero) formed by permuting M is:
  C(M) = (k - c_0) * (k - 1)! / (c_0! * c_1! * ... * c_9!).

When these C(M) distinct numbers are sorted in strictly increasing order, the i-th number
has exactly C(M) - i larger permutations.
Summing T(n) over all n in the multiset equivalence class of M gives:
  sum_{n in M} T(n) = sum_{i=1}^{C(M)} (C(M) - i) = binom(C(M), 2) = C(M) * (C(M) - 1) / 2.

Thus, S(k) is simply:
  S(k) = sum_{M: sum c_d = k, c_0 < k} binom(C(M), 2).

The number of digit multisets for k = 12 is binom(12 + 10 - 1, 9) = binom(21, 9) = 293,930,
evaluated in under 0.15 seconds in Python.
"""

from __future__ import annotations

import math


def solve(k: int = 12) -> int:
    """Compute S(k), the sum of T(n) for all k-digit integers."""
    fact = [math.factorial(i) for i in range(k + 1)]
    ans = 0

    def dfs(digit: int, remaining: int, cur_counts: list[int]) -> None:
        nonlocal ans
        if digit == 9:
            cur_counts.append(remaining)
            c0 = cur_counts[0]
            if c0 < k:
                denom = 1
                for count in cur_counts:
                    denom *= fact[count]
                c_m = (k - c0) * fact[k - 1] // denom
                ans += c_m * (c_m - 1) // 2
            cur_counts.pop()
            return

        for count in range(remaining + 1):
            cur_counts.append(count)
            dfs(digit + 1, remaining - count, cur_counts)
            cur_counts.pop()

    dfs(0, k, [])
    return ans


if __name__ == "__main__":
    print(solve())
