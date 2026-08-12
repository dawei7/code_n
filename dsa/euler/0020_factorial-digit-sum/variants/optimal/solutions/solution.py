import math


def solve(n: int = 100) -> int:
    """Find sum of the digits in n!.
    
    Time Complexity: O(M)
    Space Complexity: O(M)
    """
    return sum(int(d) for d in str(math.factorial(n)))
