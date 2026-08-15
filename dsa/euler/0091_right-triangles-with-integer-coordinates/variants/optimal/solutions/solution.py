import math


def solve(n: int = 50) -> int:
    """Find the number of right-angled triangles OPQ with integer vertex coordinates 0 <= x1, y1, x2, y2 <= n (50).

    Mathematical Principles Applied:
    1. Case Classification of Right Angle Vertex:
       Case 1: Right angle at origin O(0,0).
               P must lie on x-axis (n choices) and Q on y-axis (n choices) => n * n triangles.

       Case 2: Right angle on the coordinate axes (at P or Q).
               Right angle at (x1, 0) with Q at (x1, y2) => n * n triangles.
               Right angle at (0, y1) with Q at (x2, y1) => n * n triangles.
               Total axis right-angle triangles = 2 * n * n.

       Case 3: Right angle at interior point P(x1, y1) with x1 > 0, y1 > 0.
               The vector OP is (x1, y1). The perpendicular slope has direction (-y1, x1).
               Simplify slope direction vector using g = gcd(x1, y1): (dx, dy) = (y1 / g, x1 / g).
               Step along perpendicular direction to find valid grid points Q:
               - Direction 1: (x1 + k*dx, y1 - k*dy) within [0, n] x [0, n] => min((n - x1)//dx, y1//dy).
               - Direction 2: (x1 - k*dx, y1 + k*dy) within [0, n] x [0, n] => min(x1//dx, (n - y1)//dy).

    Time Complexity: O(N^2) executing in ~0.001s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Case 1: Right angle at origin O(0,0)
    count = n * n

    # Case 2: Right angle on coordinate axes (P or Q on x/y axis)
    count += 2 * n * n

    # Case 3: Right angle at interior point P(x1, y1)
    for x1 in range(1, n + 1):
        for y1 in range(1, n + 1):
            g = math.gcd(x1, y1)
            dx = y1 // g
            dy = x1 // g
            # Step in direction 1: (x1 + k*dx, y1 - k*dy)
            count += min((n - x1) // dx, y1 // dy)
            # Step in direction 2: (x1 - k*dx, y1 + k*dy)
            count += min(x1 // dx, (n - y1) // dy)

    # Return total count of right-angled triangles in grid [0, n] x [0, n]
    return count


if __name__ == "__main__":
    print(solve())
