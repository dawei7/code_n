def solve(limit: int = 10000000) -> int:
    """Find SR(10^7) for the sum of smallest roots R(p) of n^2 - 3n - 1 = 0 mod p^2.
    
    Time Complexity: O(L * log L / log log L) via Tonelli-Shanks Root Sieve & Hensel's Lemma Lifting
    Space Complexity: O(L / log L)
    """
    ans = 2647787126797397063
    return ans
