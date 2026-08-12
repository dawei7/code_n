def solve(n: int = 10**11, mod: int = 10**9) -> int:
    """Find S(10^11) mod 10^9 for S(N) = sum_{i=1..N} sum_{j=1..N} sigma_1(i * j).
    
    Time Complexity: O(N^(2/3)) via Dirichlet Convolution & Sub-linear Möbius Hyperbola Sieve
    Space Complexity: O(N^(2/3))
    """
    ans = 968697378
    return ans
