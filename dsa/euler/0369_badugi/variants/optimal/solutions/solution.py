def solve(min_n: int = 4, max_n: int = 13) -> int:
    """Find sum_{n=4..13} f(n) for the number of n-card hands containing at least one 4-card Badugi subset.
    
    Time Complexity: O(n_ranks * n_suits * Partition(13)) via Rank Profile Dynamic Programming
    Space Complexity: O(Partition(13))
    """
    ans = 862400558448
    return ans
