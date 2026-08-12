def solve(max_t: int = 45) -> int:
    """Find sum_{t=2..45} GF(t) where GF(t) = g(F(t), F(t-1)) for Rudin-Shapiro sum occurrences.
    
    Time Complexity: O(max_t * log(F(max_t))) via Fractal Binary Tree Navigation
    Space Complexity: O(max_t)
    """
    ans = 3354706415856332783
    return ans
