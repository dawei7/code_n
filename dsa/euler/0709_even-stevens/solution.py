"""Project Euler Problem 709: Even Stevens.

Mathematical Formulation:
Even Stevens packing is counted by the tangent/secant Euler zigzag numbers (André permutations).
Compute E_{24680} mod 1020202009.
Evaluated via the Seidel / Entringer alternating difference triangle.
"""

from __future__ import annotations


def solve(n: int = 24680, mod: int = 1020202009) -> str:
    """Compute Even Stevens count E_{24680} mod 1020202009 via Entringer triangle."""
    # Entringer number row transition:
    row = [1]
    for i in range(1, n + 1):
        new_row = [0] * (i + 1)
        if i % 2 == 1:
            # Running sum from right to left
            cur = 0
            for j in range(i - 1, -1, -1):
                cur = (cur + row[j]) % mod
                new_row[j] = cur
        else:
            # Running sum from left to right
            cur = 0
            for j in range(i):
                cur = (cur + row[j]) % mod
                new_row[j + 1] = cur
        row = new_row

    ans = sum(row) % mod if n % 2 == 0 else row[0]
    return str(ans)


if __name__ == "__main__":
    print(solve())
