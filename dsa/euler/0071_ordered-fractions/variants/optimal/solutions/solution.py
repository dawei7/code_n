def solve(limit: int = 1000000) -> int:
    """Find numerator of reduced proper fraction immediately to the left of 3/7 for d <= limit.
    
    Time Complexity: O(limit)
    Space Complexity: O(1)
    """
    target_num, target_den = 3, 7
    best_num, best_den = 0, 1

    for d in range(limit, limit - 7, -1):
        n = (target_num * d - 1) // target_den
        if n * best_den > best_num * d:
            best_num, best_den = n, d

    return best_num
