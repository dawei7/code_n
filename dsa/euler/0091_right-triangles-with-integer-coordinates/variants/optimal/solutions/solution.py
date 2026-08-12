import math


def solve(n: int = 50) -> int:
    """Find number of right triangles OPQ with 0 <= x1, y1, x2, y2 <= n.
    
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    # 1. Right angle at origin O(0,0)
    count = n * n

    # 2. Right angle on axes (P on x-axis/y-axis)
    count += 2 * n * n

    # 3. Right angle at P(x1, y1) with x1 > 0, y1 > 0
    for x1 in range(1, n + 1):
        for y1 in range(1, n + 1):
            g = math.gcd(x1, y1)
            dx = y1 // g
            dy = x1 // g
            # Step in direction 1: (x1 + dx, y1 - dy)
            count += min((n - x1) // dx, y1 // dy)
            # Step in direction 2: (x1 - dx, y1 + dy)
            count += min(x1 // dx, (n - y1) // dy)

    return count
