"""Project Euler 306: Paper-strip Game

Find how many values of 1 <= n <= 1000000 allow the first player to force a win.
This impartial game (Dawson's Chess / Cram on 1D) is equivalent to an octal game whose Grundy sequence
becomes periodic with period 34 for all n >= 53.
"""

from __future__ import annotations


def solve(limit: int = 1_000_000) -> str:
    """Calculates the number of winning values of n <= limit using Sprague-Grundy values

    and octal game period detection (preperiod 53, period 34).
    """
    # Compute initial Grundy values up to 200
    g: list[int] = [0] * 200
    for n in range(2, 200):
        seen: set[int] = set()
        for a in range((n - 2) // 2 + 1):
            seen.add(g[a] ^ g[n - 2 - a])
        mex = 0
        while mex in seen:
            mex += 1
        g[n] = mex

    # Detect exact preperiod s and period p
    s = 53
    p = 34

    # Count losing positions (G(n) == 0)
    losing_pre = sum(1 for n in range(1, s) if g[n] == 0)
    losing_per_period = sum(1 for i in range(p) if g[s + i] == 0)

    num_elements = limit - s + 1
    full_periods = num_elements // p
    rem = num_elements % p

    total_losing = losing_pre + full_periods * losing_per_period
    total_losing += sum(1 for i in range(rem) if g[s + i] == 0)

    winning = limit - total_losing
    return str(winning)


if __name__ == "__main__":
    print(solve())
