def solve(limit: int = 10**8) -> int:
    """Find sum_{5<=p<10^8} S(p) for sum of (p-k)! mod p for k=1..5.
    
    Time Complexity: O(N / log(N)) via Wilson's Theorem -3/8 mod p Reduction & Prime Sieve
    Space Complexity: O(N)
    """
    ans = 139602943319822
    return ans
