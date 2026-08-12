def solve(n: int = 50) -> int:
    """Find number of ways to tile a row of length n using grey (1), red (2), green (3), and blue (4) tiles.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] += dp[i - 1]  # Grey tile (1)
        if i >= 2:
            dp[i] += dp[i - 2]  # Red tile (2)
        if i >= 3:
            dp[i] += dp[i - 3]  # Green tile (3)
        if i >= 4:
            dp[i] += dp[i - 4]  # Blue tile (4)

    return dp[n]
