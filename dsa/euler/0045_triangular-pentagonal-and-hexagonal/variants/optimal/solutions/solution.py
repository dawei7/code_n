import math


def is_pentagonal(p: int) -> bool:
    """Check if p is pentagonal P_n = n(3n-1)/2."""
    val = 1 + 24 * p
    root = math.isqrt(val)
    return root * root == val and root % 6 == 5


def solve(start_h: int = 144) -> int:
    """Find next number after T_285 = P_165 = H_143 = 40755 that is Triangular, Pentagonal, and Hexagonal.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    # Note: Every hexagonal number H_m is automatically triangular T_(2m-1).
    m = start_h
    while True:
        h = m * (2 * m - 1)
        if is_pentagonal(h):
            return h
        m += 1
