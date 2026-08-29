"""Project Euler Problem 577: Counting Hexagons.

Find sum_{n=3..12345} H(n), where H(n) is the number of regular hexagons formed
by the vertices of an equilateral triangular lattice of side length n.
"""


def _h_single(n: int) -> int:
    """Compute H(n) for an equilateral triangle of side length n."""
    return sum(
        k * (n - 3 * k + 1) * (n - 3 * k + 2) // 2
        for k in range(1, n // 3 + 1)
    )


def solve(limit: int = 12345) -> int:
    """Compute sum_{n=3..limit} H(n) using tetrahedral hockey-stick identity in O(limit/3)."""
    return sum(
        k * (limit - 3 * k + 1) * (limit - 3 * k + 2) * (limit - 3 * k + 3) // 6
        for k in range(1, limit // 3 + 1)
    )


if __name__ == "__main__":
    print(solve())
