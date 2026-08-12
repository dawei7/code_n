def solve(limit: int = 1000) -> int:
    """Find last ten digits of series 1^1 + 2^2 + ... + 1000^1000 using modular exponentiation.
    
    Time Complexity: O(limit * log limit)
    Space Complexity: O(1)
    """
    mod = 10**10
    return sum(pow(i, i, mod) for i in range(1, limit + 1)) % mod
