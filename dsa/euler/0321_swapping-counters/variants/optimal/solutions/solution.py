"""Project Euler 321: Swapping Counters

Find the sum of the first 40 terms of the sequence of integers n for which
the minimum number of moves M(n) = n(n + 2) is a triangle number.
"""

from __future__ import annotations


def solve(target_count: int = 40) -> str:
    """Calculates the sum of the first target_count terms of the sequence of integers n

    for which M(n) = n(n + 2) is a triangle number m(m + 1) / 2 using the generalized Pell equation
    X^2 - 2y^2 = -7 with X = 2m + 1, y = 2n + 2, and unit fundamental multiplier (3 + 2*sqrt(2)).
    """
    # Base solution classes (X0, y0) to X^2 - 2y^2 = -7
    base_classes = [(1, 2), (-1, 2), (5, 4), (-5, 4)]
    n_values: set[int] = set()

    for x0, y0 in base_classes:
        x, y = x0, y0
        for _ in range(target_count + 5):
            if y % 2 == 0 and x % 2 == 1:
                n = (y - 2) // 2
                m = (x - 1) // 2
                if n > 0 and m > 0 and n * (n + 2) == m * (m + 1) // 2:
                    n_values.add(n)

            # Advance along the Pell hyperbolas via (3 + 2*sqrt(2))
            x_next = 3 * x + 4 * y
            y_next = 2 * x + 3 * y
            x, y = x_next, y_next

    sorted_n = sorted(n_values)
    ans = sum(sorted_n[:target_count])
    return str(ans)


if __name__ == "__main__":
    print(solve())
