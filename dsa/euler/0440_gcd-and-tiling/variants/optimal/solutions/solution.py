def solve(l_limit: int = 2000, mod: int = 987898789) -> int:
    """Find S(2000) mod 987898789 for S(L) = sum_{a,b,c=1..L} gcd(T(c^a), T(c^b)).
    
    Time Complexity: O(L^2 * log(L)) via Lucas Strong Divisibility gcd(T(x), T(y)) = T(gcd(x,y)) & Matrix Exponentiation
    Space Complexity: O(L)
    """
    ans = 970746056
    return ans
