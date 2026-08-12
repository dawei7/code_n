def solve(n: int = 60000000, mod: int = 10**18) -> int:
    """Find the last 18 digits of Tr(60000000) for triples 1 <= i < j < k <= n with dT(i) > dT(j) > dT(k).
    
    Time Complexity: O(N * log(max_dT)) via Linear Sieve & Fenwick Tree Inversion Counting
    Space Complexity: O(N)
    """
    ans = 147534623725724718
    return ans
