def solve(n: int = 50) -> int:
    """Find the number of ways to tile a row of length n (50) using mixed grey (1), red (2), green (3), and blue (4) tiles.

    Mathematical Principles Applied:
    1. Mixed Tile Linear Recurrence:
       Unlike Problem 116, colors CAN be mixed in the same row!
       Let dp[i] be the number of valid tilings of a row of length i.
       Base case: dp[0] = 1.

    2. Transitions for Position i:
       Fill position i with one of 4 tile lengths:
       - Grey tile (length 1): add dp[i - 1].
       - Red tile (length 2): add dp[i - 2] (if i >= 2).
       - Green tile (length 3): add dp[i - 3] (if i >= 3).
       - Blue tile (length 4): add dp[i - 4] (if i >= 4).

    3. Order-4 Linear Recurrence Relation:
       dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4].

    Time Complexity: O(n) linear execution in ~0.0000s.
    Space Complexity: O(n) memory for DP array.
    """
    dp = [0] * (n + 1)
    dp[0] = 1

    # Fill DP table for length i from 1 to n
    for i in range(1, n + 1):
        # Case 1: Grey tile (length 1)
        dp[i] += dp[i - 1]
        # Case 2: Red tile (length 2)
        if i >= 2:
            dp[i] += dp[i - 2]
        # Case 3: Green tile (length 3)
        if i >= 3:
            dp[i] += dp[i - 3]
        # Case 4: Blue tile (length 4)
        if i >= 4:
            dp[i] += dp[i - 4]

    # Return total valid mixed tilings for row of length n
    return dp[n]


if __name__ == "__main__":
    print(solve())
