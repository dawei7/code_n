def solve(n: int = 100) -> int:
    """Find difference between square of sum and sum of squares for first n natural numbers.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    sum_n = n * (n + 1) // 2
    sq_sum = sum_n * sum_n
    sum_sq = n * (n + 1) * (2 * n + 1) // 6
    return sq_sum - sum_sq
