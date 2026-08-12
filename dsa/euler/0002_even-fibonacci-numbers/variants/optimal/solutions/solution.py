def solve(limit: int = 4000000) -> int:
    """Sum of even-valued Fibonacci terms up to limit using recurrence E_n = 4*E_{n-1} + E_{n-2}.
    
    Time Complexity: O(log limit)
    Space Complexity: O(1)
    """
    total = 0
    a, b = 2, 8
    while a <= limit:
        total += a
        a, b = b, 4 * b + a
    return total
