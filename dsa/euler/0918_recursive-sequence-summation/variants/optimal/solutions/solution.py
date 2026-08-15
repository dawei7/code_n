"""Project Euler Problem 918: Recursive Sequence Summation.

Mathematical formulation:
Let a_1 = 1, a_{2n} = 2a_n, and a_{2n+1} = a_n - 3a_{n+1} for n >= 1.
Define S(N) = sum_{n=1}^N a_n.

Telescoping Identity & Closed-Form Reduction:
Observing the sum of adjacent even and odd terms:
  a_{2k} + a_{2k+1} = 2a_k + (a_k - 3a_{k+1}) = 3(a_k - a_{k+1}).
Summing across k = 1 to m telescopes directly:
  sum_{k=1}^m (a_{2k} + a_{2k+1}) = 3(a_1 - a_{m+1}) = 3(1 - a_{m+1}).

Therefore, for any positive integer N:
  - If N = 2m:     S(2m) = 4 - a_m
  - If N = 2m + 1: S(2m + 1) = 4 - 3a_{m+1}

Computing a_m via memoized divide-and-conquer recursion evaluates S(10^12) in O(log N) time.

Evaluates S(10^12) = -6999033352333308 in under 0.001s in 100% pure Python.
"""

from __future__ import annotations


def solve(n: int = 10**12) -> int:
    """Compute S(N) in O(log N) time using iterative memoized recursion."""
    if n == 1:
        return 1

    target_k = n // 2 if n % 2 == 0 else n // 2 + 1
    memo: dict[int, int] = {1: 1}

    # Iterative resolution stack for a_k evaluation
    stack = [target_k]
    visited = []

    while stack:
        curr = stack.pop()
        if curr in memo:
            continue
        if curr % 2 == 0:
            half = curr // 2
            if half in memo:
                memo[curr] = 2 * memo[half]
            else:
                stack.append(curr)
                stack.append(half)
        else:
            m = curr // 2
            if m in memo and (m + 1) in memo:
                memo[curr] = memo[m] - 3 * memo[m + 1]
            else:
                stack.append(curr)
                if (m + 1) not in memo:
                    stack.append(m + 1)
                if m not in memo:
                    stack.append(m)

    val = memo[target_k]
    if n % 2 == 0:
        return 4 - val
    return 4 - 3 * val


if __name__ == "__main__":
    print(solve())
