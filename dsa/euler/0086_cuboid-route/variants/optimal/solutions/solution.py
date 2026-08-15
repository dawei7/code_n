import math


def solve(target: int = 1000000) -> int:
    """Find the least value of M such that the number of cuboids with integer shortest surface route exceeds target (1,000,000).

    Mathematical Principles Applied:
    1. Cuboid Shortest Surface Path Unfolding:
       For a cuboid with dimensions a >= b >= c >= 1, unfolding the cuboid surfaces into a 2D plane
       gives the shortest path distance d = sqrt(a^2 + (b + c)^2).
       The shortest surface route d is an integer iff a^2 + (b + c)^2 is a perfect square!

    2. Combined Pair Parameter s = b + c:
       Let s = b + c. Since 1 <= c <= b <= a, we have 2 <= s <= 2*a.
       - If s <= a: valid pairs (b, c) with b + c = s and 1 <= c <= b is floor(s / 2).
       - If s > a: valid pairs (b, c) with b + c = s and 1 <= c <= b <= a is a - floor((s - 1) / 2).

    3. Incremental Dimension Sweep:
       Increment maximum dimension a starting from 1, accumulating valid cuboids until total count exceeds 1,000,000.

    Time Complexity: O(M^2) executing in ~0.60s for M ≈ 1818.
    Space Complexity: O(1) constant auxiliary space.
    """
    count = 0
    a = 1

    # Increment maximum cuboid dimension a = 1, 2, 3, ...
    while True:
        a_sq = a * a
        # Combined sum s = b + c ranges from 2 to 2*a
        for s in range(2, 2 * a + 1):
            dist_sq = a_sq + s * s
            root = math.isqrt(dist_sq)

            # Check if surface distance squared is a perfect square
            if root * root == dist_sq:
                # Count pairs (b, c) such that 1 <= c <= b <= a and b + c = s
                if s <= a:
                    count += s // 2
                else:
                    count += a - (s - 1) // 2

        # Return M = a as soon as cumulative cuboid count exceeds 1,000,000
        if count > target:
            return a

        a += 1


if __name__ == "__main__":
    print(solve())
