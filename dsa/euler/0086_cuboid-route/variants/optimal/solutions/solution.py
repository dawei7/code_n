import math


def solve(target: int = 1000000) -> int:
    """Find least M such that number of cuboids with integer shortest surface route exceeds target.
    
    Time Complexity: O(M^2)
    Space Complexity: O(1)
    """
    count = 0
    a = 1

    while True:
        a_sq = a * a
        for s in range(2, 2 * a + 1):
            dist_sq = a_sq + s * s
            root = math.isqrt(dist_sq)
            if root * root == dist_sq:
                if s <= a:
                    count += s // 2
                else:
                    count += a - (s - 1) // 2

        if count > target:
            return a
        a += 1
