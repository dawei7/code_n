"""Project Euler Problem 879: Touch Screen Password.

Mathematical Formulation:
Count valid password patterns of length >= 1 on a 4 x 4 grid.
A move from u to v is valid if all collinear grid points between u and v
have already been visited.
Evaluated via bitmask dynamic programming over 2^16 states.
"""

from __future__ import annotations


def solve(grid_size: int = 16) -> str:
    """Compute valid pattern password count on 4x4 grid."""
    # Precompute intermediate blockers for all pairs of keys (0..15)
    blockers = [[0] * 16 for _ in range(16)]
    for i in range(16):
        r1, c1 = divmod(i, 4)
        for j in range(16):
            if i == j:
                continue
            r2, c2 = divmod(j, 4)
            dr = r2 - r1
            dc = c2 - c1
            import math
            g = math.gcd(abs(dr), abs(dc))
            step_r = dr // g
            step_c = dc // g
            mask = 0
            cur_r, cur_c = r1 + step_r, c1 + step_c
            while (cur_r, cur_c) != (r2, c2):
                mask |= 1 << (cur_r * 4 + cur_c)
                cur_r += step_r
                cur_c += step_c
            blockers[i][j] = mask

    # Bitmask DP: dp[mask][last_key]
    dp = [[0] * 16 for _ in range(1 << 16)]
    for i in range(16):
        dp[1 << i][i] = 1

    total_patterns = 0
    for mask in range(1, 1 << 16):
        for last in range(16):
            cnt = dp[mask][last]
            if cnt == 0:
                continue
            total_patterns += cnt
            for nxt in range(16):
                if not (mask & (1 << nxt)):
                    if (mask & blockers[last][nxt]) == blockers[last][nxt]:
                        dp[mask | (1 << nxt)][nxt] += cnt

    return str(total_patterns)


if __name__ == "__main__":
    print(solve())
