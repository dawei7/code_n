import math


def solve(n: int = 20) -> int:
    """Number of lattice paths in an n x n grid using binomial coefficient (2n choose n).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    return math.comb(2 * n, n)
