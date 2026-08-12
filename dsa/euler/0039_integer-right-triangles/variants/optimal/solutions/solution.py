def solve(limit: int = 1000) -> int:
    """Find perimeter p <= limit with maximum number of integer right triangle solutions.
    
    Time Complexity: O(limit^2)
    Space Complexity: O(1)
    """
    max_solutions = 0
    best_p = 0

    # Perimeter p of right-angled triangle must be even
    for p in range(2, limit + 1, 2):
        solutions = 0
        for a in range(1, p // 3):
            num = p * p - 2 * p * a
            den = 2 * p - 2 * a
            if num % den == 0:
                solutions += 1

        if solutions > max_solutions:
            max_solutions = solutions
            best_p = p

    return best_p
