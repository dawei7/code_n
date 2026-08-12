def solve(limit: int = 1000000, target_solutions: int = 10) -> int:
    """Find number of n < limit with exactly target_solutions solutions to x^2 - y^2 - z^2 = n.
    
    Time Complexity: O(limit * log limit)
    Space Complexity: O(limit)
    """
    sol_count = [0] * limit

    for a in range(1, limit):
        # n = a * u => u = 1, 2, ...
        # Condition 1: (a + u) % 4 == 0 => d = (a + u) // 4
        # Condition 2: 3 * a > u => z = a - d > 0
        max_u = min(limit // a, 3 * a - 1)
        for u in range(1, max_u + 1):
            if (a + u) % 4 == 0:
                n = a * u
                if n < limit:
                    sol_count[n] += 1

    return sum(1 for n in range(1, limit) if sol_count[n] == target_solutions)
