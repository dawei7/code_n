def solve(n: int = 50, m: int = 3) -> int:
    """Find number of ways to fill a row of length n with red blocks of min length m.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        # Position i is a grey square
        dp[i] = dp[i - 1]

        # Red block of length len >= m ending at position i
        for length in range(m, i + 1):
            if i - length - 1 >= 0:
                dp[i] += dp[i - length - 1]
            else:
                dp[i] += 1  # Red block spans to start of row

    return dp[n]
