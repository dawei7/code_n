import math


def solve(d: int = 100) -> int:
    """Find number of non-bouncy numbers below 10^d using stars and bars combinatorics.
    
    Time Complexity: O(d)
    Space Complexity: O(1)
    """
    increasing = math.comb(d + 9, 9) - 1
    decreasing = math.comb(d + 10, 10) - 1 - d
    overlap = 9 * d

    return increasing + decreasing - overlap
