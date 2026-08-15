"""Project Euler Problem 366: Stone Game III.

Find sum_{n <= 10^18} M(n) mod 10^8, where M(n) is the maximum number of stones
the first player can take on the first turn of Fibonacci Nim to guarantee a win.
"""

from typing import Dict


def solve(limit: int = 10**18, mod: int = 10**8) -> int:
    """Compute sum_{n <= limit} M(n) mod 10^8 using logarithmic Fibonacci interval recursion."""
    if limit <= 3:
        return 0

    # Precompute Fibonacci sequence up to > 2 * limit
    fibs = [0, 1, 1]
    while fibs[-1] <= 2 * limit:
        fibs.append(fibs[-1] + fibs[-2])

    memo: Dict[int, int] = {}

    def tri_sum(m_val: int) -> int:
        return (m_val * (m_val + 1) // 2) % mod

    def prefix_sum(n: int) -> int:
        if n <= 3:
            return 0
        if n in memo:
            return memo[n]

        # Find largest Fibonacci number <= n
        idx = 2
        while idx + 1 < len(fibs) and fibs[idx + 1] <= n:
            idx += 1
        fk = fibs[idx]
        r = n - fk
        cutoff = (fk - 1) // 2

        if r == 0:
            # Full Fibonacci interval reduction: S(F_i) = S(F_{i-1}) + tri_sum(cutoff_{i-1}) + S(F_{i-2}) - S(cutoff_{i-1})
            prev_fk = fibs[idx - 1]
            prev_cutoff = (prev_fk - 1) // 2
            res = (
                prefix_sum(prev_fk)
                + tri_sum(prev_cutoff)
                + prefix_sum(fibs[idx - 2])
                - prefix_sum(prev_cutoff)
            ) % mod
            memo[n] = res
            return res

        s_fk = prefix_sum(fk)
        m = min(r, cutoff)
        res = (s_fk + tri_sum(m)) % mod
        if r > cutoff:
            res = (res + prefix_sum(r) - prefix_sum(cutoff)) % mod

        memo[n] = res
        return res

    return prefix_sum(limit)


if __name__ == "__main__":
    print(solve())
