def solve(limit: int = 1000000000000) -> int:
    """Find number of blue discs b in the first arrangement with total discs N > limit where P(BB) = 1/2.
    
    Time Complexity: O(log limit)
    Space Complexity: O(1)
    """
    b, n = 15, 21

    while n <= limit:
        b_next = 3 * b + 2 * n - 2
        n_next = 4 * b + 3 * n - 3
        b, n = b_next, n_next

    return b
