"""Project Euler Problem 653: Frictionless Tube.

Find d(1000000000, 1000001, 500001), where d(L, N, j) is the distance in millimetres
that the j-th marble travels before its centre reaches the eastern end of the tube.
"""

_MOD = 32_745_673


def solve(l_tube: int = 1_000_000_000, n: int = 1_000_001, j: int = 500_001) -> int:
    """Compute d(L, N, j) using the point-mass contact contraction and ray-tracing order invariance."""
    r = 6_563_116
    y = 0
    a = [0] * n

    for i in range(n):
        g = (r % 1000) + 1
        y += g
        a[i] = -y if r <= 10_000_000 else y
        r = (r * r) % _MOD

    m = n - j + 1
    a.sort()
    am = a[m - 1]

    return (l_tube - 20 * j + 10) + am


if __name__ == "__main__":
    print(solve())
