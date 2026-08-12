import math


def solve(n: int = 20) -> int:
    """Find the smallest multiple of all numbers from 1 to n using LCM.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    return math.lcm(*range(1, n + 1))
