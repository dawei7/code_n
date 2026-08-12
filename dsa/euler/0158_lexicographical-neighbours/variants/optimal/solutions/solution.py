import math


def p(n: int) -> int:
    """Find number of strings of length n with distinct letters having exactly 1 lexicographical increase."""
    return math.comb(26, n) * (2**n - n - 1)


def solve() -> int:
    """Find maximum value of p(n) for 1 <= n <= 26.
    
    Time Complexity: O(N) where N = 26
    Space Complexity: O(1)
    """
    return max(p(n) for n in range(1, 27))
