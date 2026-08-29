"""Project Euler Problem 706: 3-Like Numbers.

Find F(10^5) mod 1000000007, the number of d-digit positive integers such that the number of
substrings divisible by 3 is itself divisible by 3.
"""

from typing import Dict, Tuple

_MOD = 1_000_000_007


def solve(d: int = 100_000) -> int:
    """Compute F(d) mod 1000000007 using 27-state prefix sum residue dynamic programming."""
    dp: Dict[Tuple[int, int, int, int], int] = {(0, 1, 0, 0): 1}

    for step in range(1, d + 1):
        new_dp: Dict[Tuple[int, int, int, int], int] = {}
        digit_counts = {0: 3, 1: 3, 2: 3} if step == 1 else {0: 4, 1: 3, 2: 3}

        for (r, c0, c1, c2), ways in dp.items():
            for m3, cnt in digit_counts.items():
                nr = (r + m3) % 3
                nc0 = (c0 + (1 if nr == 0 else 0)) % 3
                nc1 = (c1 + (1 if nr == 1 else 0)) % 3
                nc2 = (c2 + (1 if nr == 2 else 0)) % 3
                nstate = (nr, nc0, nc1, nc2)
                new_dp[nstate] = (new_dp.get(nstate, 0) + ways * cnt) % _MOD

        dp = new_dp

    ans = 0
    for (_, c0, c1, c2), ways in dp.items():
        k2 = (1 if c0 == 2 else 0) + (1 if c1 == 2 else 0) + (1 if c2 == 2 else 0)
        if k2 % 3 == 0:
            ans = (ans + ways) % _MOD

    return ans


if __name__ == "__main__":
    print(solve())
