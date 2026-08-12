def solve(limit: int = 1000000) -> int:
    """Find the value of n <= limit for which n/phi(n) is a maximum.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    n = 1
    for p in primes:
        if n * p > limit:
            break
        n *= p
    return n
