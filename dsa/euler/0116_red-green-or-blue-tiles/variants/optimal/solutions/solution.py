def solve(n: int = 50) -> int:
    """Find total ways to replace grey tiles in a row of length n (50) with red (2), green (3), or blue (4) tiles.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Independent Color Tile Replacement:
       Colours cannot be mixed in a single row.
       We evaluate the number of ways to tile a row of length n using:
       - Red tiles of fixed length 2 (and grey tiles of length 1)
       - Green tiles of fixed length 3 (and grey tiles of length 1)
       - Blue tiles of fixed length 4 (and grey tiles of length 1)
       At least one colored tile must be used.

    2. Linear Dynamic Programming Recurrence:
       For a fixed tile length L in {2, 3, 4}:
       Let dp[i] be the number of ways to fill a row of length i.
       - Case 1: Position i is grey -> dp[i-1] ways.
       - Case 2: Position i is covered by a colored tile of length L -> dp[i-L] ways (if i >= L).
       Recurrence: dp[i] = dp[i-1] + (dp[i-L] if i >= L else 0).
       Total non-empty ways = dp[n] - 1 (subtracting the all-grey configuration).

    3. Combined Total:
       TotalWays = (dp_2[n] - 1) + (dp_3[n] - 1) + (dp_4[n] - 1).

    Complexity:
    -----------
    - Time Complexity: O(n) linear execution in ~0.0000s.
    - Space Complexity: O(n) memory for DP array.
    """
    total_ways = 0

    # Evaluate each tile size independently
    for tile_len in (2, 3, 4):
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if i >= tile_len:
                dp[i] += dp[i - tile_len]

        # Subtract 1 to exclude the all-grey configuration (must use at least one colored tile)
        total_ways += dp[n] - 1

    return total_ways


if __name__ == "__main__":
    print(solve())
