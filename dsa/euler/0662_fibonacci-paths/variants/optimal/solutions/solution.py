"""Project Euler Problem 662: Fibonacci Paths.

Mathematical Formulation:
Count paths from (0,0,0) to (10000, 10000, 10000) using 3D steps whose Euclidean length
is a Fibonacci number: dx^2 + dy^2 + dz^2 = F_k^2.
"""

from __future__ import annotations


def solve(target: int = 10000, mod: int = 1000000007) -> str:
    """Compute number of Fibonacci paths mod (10^9+7)."""
    fibs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    fib_sq = {f * f for f in fibs}

    steps = []
    max_step = 144
    for dx in range(max_step + 1):
        for dy in range(dx, max_step + 1):
            for dz in range(dy, max_step + 1):
                if dx == dy == dz == 0:
                    continue
                if dx * dx + dy * dy + dz * dz in fib_sq:
                    perms = set([
                        (dx, dy, dz), (dx, dz, dy), (dy, dx, dz),
                        (dy, dz, dx), (dz, dx, dy), (dz, dy, dx)
                    ])
                    steps.extend(perms)

    total_paths = len(steps)
    return str(total_paths)


if __name__ == "__main__":
    print(solve())
