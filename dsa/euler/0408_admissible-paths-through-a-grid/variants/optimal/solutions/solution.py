"""Project Euler Problem 408: Admissible Paths Through a Grid.

Find P(10^7) mod 1,000,000,007, where P(n) is the number of admissible paths
from (0, 0) to (n, n) avoiding points where x, y, and x+y are perfect squares.
"""

from math import gcd, isqrt
from typing import List, Tuple


def solve(n_val: int = 10_000_000, mod: int = 1_000_000_007) -> int:
    """Compute P(n_val) mod mod using obstacle inclusion-exclusion dynamic programming."""
    u_max = isqrt(n_val)
    pts_set = set()

    # Generate Pythagorean triples u^2 + v^2 = w^2 with u, v <= u_max
    for m in range(2, u_max + 1):
        for n_sub in range(1, m):
            if (m - n_sub) % 2 == 1 and gcd(m, n_sub) == 1:
                u0 = m * m - n_sub * n_sub
                v0 = 2 * m * n_sub
                k = 1
                while True:
                    u = k * u0
                    v = k * v0
                    if u > u_max and v > u_max:
                        break
                    if u <= u_max and v <= u_max:
                        pts_set.add((u * u, v * v))
                        pts_set.add((v * v, u * u))
                    k += 1

    pts: List[Tuple[int, int]] = sorted(
        pts_set, key=lambda p: (p[0] + p[1], p[0])
    )
    pts.append((n_val, n_val))
    num_obstacles = len(pts)

    # Precompute factorials up to 2 * n_val
    max_fact = 2 * n_val
    fact = [1] * (max_fact + 1)
    for i in range(1, max_fact + 1):
        fact[i] = (fact[i - 1] * i) % mod

    inv = [1] * (max_fact + 1)
    inv[max_fact] = pow(fact[max_fact], mod - 2, mod)
    for i in range(max_fact - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % mod

    def paths(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if dx < 0 or dy < 0:
            return 0
        total_steps = dx + dy
        return (fact[total_steps] * inv[dx] % mod) * inv[dy] % mod

    # dp[i] = number of admissible paths from (0, 0) to pts[i] without visiting any other obstacle
    dp = [0] * num_obstacles
    origin = (0, 0)

    for i in range(num_obstacles):
        pt_i = pts[i]
        val = paths(origin, pt_i)
        xi, yi = pt_i
        for j in range(i):
            xj, yj = pts[j]
            if xj <= xi and yj <= yi:
                val = (val - dp[j] * paths(pts[j], pt_i)) % mod
        dp[i] = val

    return dp[-1] % mod


if __name__ == "__main__":
    print(solve())
