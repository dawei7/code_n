def r_max(a: int) -> int:
    """Find maximum remainder when (a-1)^n + (a+1)^n is divided by a^2."""
    if a % 2 == 0:
        return a * (a - 2)
    else:
        return a * (a - 1)


def solve(limit: int = 1000) -> int:
    """Find sum of r_max for 3 <= a <= limit.
    
    Time Complexity: O(limit)
    Space Complexity: O(1)
    """
    return sum(r_max(a) for a in range(3, limit + 1))
