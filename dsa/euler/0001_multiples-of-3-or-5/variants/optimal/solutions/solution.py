def solve(limit: int = 1000) -> int:
    """Sum of all multiples of 3 or 5 strictly below limit using inclusion-exclusion.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    target = limit - 1

    def sum_multiples(k: int) -> int:
        p = target // k
        return k * p * (p + 1) // 2

    return sum_multiples(3) + sum_multiples(5) - sum_multiples(15)
