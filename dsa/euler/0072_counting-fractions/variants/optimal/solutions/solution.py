def solve(limit: int = 1000000) -> int:
    """Find total number of reduced proper fractions for d <= limit using totient sieve.
    
    Time Complexity: O(limit * log log limit)
    Space Complexity: O(limit)
    """
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, limit + 1, i):
                phi[j] = phi[j] // i * (i - 1)

    return sum(phi[2:])
