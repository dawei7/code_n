import math


def solve(limit: int = 12000) -> int:
    """Find number of reduced proper fractions between 1/3 and 1/2 for d <= limit.
    
    Time Complexity: O(limit^2)
    Space Complexity: O(1)
    """
    count = 0
    for d in range(4, limit + 1):
        n_min = d // 3 + 1
        n_max = (d - 1) // 2
        for n in range(n_min, n_max + 1):
            if math.gcd(n, d) == 1:
                count += 1
    return count
