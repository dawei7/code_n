def ways_for_tile_size(n: int, tile_len: int) -> int:
    """Find number of ways to fill row of length n with tiles of length 1 or tile_len."""
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if i >= tile_len:
            dp[i] += dp[i - tile_len]
    return dp[n] - 1  # Exclude all-grey configuration


def solve(n: int = 50) -> int:
    """Find total ways to replace grey tiles in row of length n using red (2), green (3), or blue (4) tiles.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return (
        ways_for_tile_size(n, 2) +
        ways_for_tile_size(n, 3) +
        ways_for_tile_size(n, 4)
    )
