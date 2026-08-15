"""Project Euler Problem 757: Stealthy Numbers.

Mathematical Formulation:
Stealthy numbers: N = a * b = c * d with a + b = c + d + 1.
Equivalent to N = x * (x + 1) * y * (y + 1) for positive integers x, y.
Count unique stealthy numbers <= 10^{14}.
"""

from __future__ import annotations

import math


def solve(limit: int = 10**14) -> str:
    """Compute number of stealthy numbers <= limit."""
    stealthy = set()
    max_x = int((math.isqrt(4 * int(math.isqrt(limit)) + 1) - 1) // 2)
    
    for x in range(1, max_x + 1):
        x_term = x * (x + 1)
        max_y = int((math.isqrt(4 * (limit // x_term) + 1) - 1) // 2)
        for y in range(x, max_y + 1):
            val = x_term * y * (y + 1)
            if val <= limit:
                stealthy.add(val)
            else:
                break
                
    return str(len(stealthy))


if __name__ == "__main__":
    print(solve())
