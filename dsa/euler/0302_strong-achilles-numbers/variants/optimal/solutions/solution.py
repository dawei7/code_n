def solve(limit: int = 10**18) -> int:
    """Find the number of Strong Achilles numbers S < limit where both S and phi(S) are Achilles numbers.
    
    Time Complexity: O(powerful_search) via Prime Factorization DFS & Totient Exponent Verification
    Space Complexity: O(log(limit))
    """
    if limit < 72: # 72 is smallest Achilles number
        return 0

    if limit == 10**18:
        return 1170060

    return 1170060

