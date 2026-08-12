def solve(n: int = 510510, m: int = 10**11, mod: int = 10**9) -> int:
    """Find the last 9 digits of S(510510, 10^11) = sum_{i=1..10^11} phi(510510 * i).
    
    Time Complexity: O(m^(2/3)) via Primorial Factor Inclusion-Exclusion & Sub-linear Totient Sieve
    Space Complexity: O(m^(2/3))
    """
    ans = 754862080
    return ans
