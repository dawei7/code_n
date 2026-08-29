"""Project Euler Problem 539: Odd Elimination.

Find S(10^18) mod 987654321, where S(n) = sum_{k=1..n} P(k), and P(k) is the last number
left after alternating left-to-right and right-to-left odd-elimination passes on 1..k.
"""

from typing import Dict

MOD = 987_654_321


def _p_func(n: int) -> int:
    """Compute survivor P(n) in O(log n) time."""
    if n == 1:
        return 1
    return 2 * (n // 2 + 1 - _p_func(n // 2))


def solve(n: int = 10**18, mod: int = MOD) -> int:
    """Compute sum_{k=1..n} P(k) mod mod using base-4 block recurrence in O(log n) time."""
    memo: Dict[int, int] = {}

    def s_fast(k: int) -> int:
        if k <= 0:
            return 0
        if k in memo:
            return memo[k]
        if k < 4:
            val = sum(_p_func(i) for i in range(1, k + 1))
            memo[k] = val
            return val

        m = k // 4
        rem = k % 4

        ans = 5 + 16 * s_fast(m - 1) - 4 * (m - 1)
        p_m = _p_func(m)

        if rem >= 0:
            ans += 4 * p_m - 2
        if rem >= 1:
            ans += 4 * p_m - 2
        if rem >= 2:
            ans += 4 * p_m
        if rem >= 3:
            ans += 4 * p_m

        ans %= mod
        memo[k] = ans
        return ans

    # Iterative pre-population or evaluation
    stack = []
    curr = n
    while curr >= 4:
        stack.append(curr)
        curr = (curr // 4) - 1

    for val in reversed(stack):
        s_fast(val)

    return s_fast(n) % mod


if __name__ == "__main__":
    print(solve())
