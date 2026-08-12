def solve(limit: int = 100) -> int:
    """Find maximum digital sum of a^b for a, b < limit.
    
    Time Complexity: O(limit^2 * D)
    Space Complexity: O(D)
    """
    return max(
        sum(int(c) for c in str(a**b))
        for a in range(1, limit)
        for b in range(1, limit)
    )
