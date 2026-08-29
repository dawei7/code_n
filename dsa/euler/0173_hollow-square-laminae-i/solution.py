import math


def solve(max_tiles: int = 1000000) -> int:
    """Find the number of different square laminae that can be formed using up to max_tiles = 1,000,000.

    Mathematical Principles Applied:
    1. Square Lamina Tiles Formula:
       A square lamina with outer side length a and inner hole side length b (a > b >= 1, a == b mod 2) uses:
       T = a^2 - b^2 = (a - b)(a + b) tiles.
       Let x = (a - b) / 2 and y = (a + b) / 2.
       Then T = 4 * x * y <= max_tiles => x * y <= max_tiles / 4 = M.

    2. Side Parity and Integer Bounds:
       Since a > b >= 1, we must have y > x >= 1.
       For each integer x from 1 up to sqrt(M):
       The number of valid y > x such that x * y <= M is given by:
       count(x) = floor(M / x) - x.

    3. Direct Hyperbola Summation:
       Total square laminae = sum_{x=1}^{floor(sqrt(M))} (floor(M / x) - x).

    Time Complexity: O(sqrt(max_tiles)) executing in ~0.0001s.
    Space Complexity: O(1) constant auxiliary space.
    """
    M = max_tiles // 4
    # Sum floor(M / x) - x over x = 1 .. sqrt(M)
    return sum(M // x - x for x in range(1, int(math.isqrt(M)) + 1))


if __name__ == "__main__":
    print(solve())
