def solve(max_b: int = 60, max_w: int = 40) -> int:
    """Find number of ways to group max_b black objects and max_w white objects.
    
    Time Complexity: O(max_b^2 * max_w^2)
    Space Complexity: O(max_b * max_w)
    """
    dp = [[0] * (max_w + 1) for _ in range(max_b + 1)]
    dp[0][0] = 1

    for i in range(max_b + 1):
        for j in range(max_w + 1):
            if i == 0 and j == 0:
                continue
            for b in range(i, max_b + 1):
                for w in range(j, max_w + 1):
                    dp[b][w] += dp[b - i][w - j]

    return dp[max_b][max_w]
