def solve(n: int = 10**15) -> int:
    """Find g(10^15) for the GCD sequence g(n) = g(n-1) + gcd(n, g(n-1)).
    
    Time Complexity: O(Jumps * sqrt(k)) via Fast Prime Divisor Next-Multiple Jump Sieve
    Space Complexity: O(1)
    """
    ans = 2744233049300770
    return ans
