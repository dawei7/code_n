def solve(n: int = 600851475143) -> int:
    """Find the largest prime factor of n using trial division.
    
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    """
    d = 2
    max_factor = 1
    while d * d <= n:
        if n % d == 0:
            max_factor = d
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        max_factor = n
    return max_factor
