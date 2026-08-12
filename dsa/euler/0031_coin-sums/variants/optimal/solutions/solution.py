def solve(target: int = 200) -> int:
    """Find number of ways to make target pence using UK coins.
    
    Time Complexity: O(C * target)
    Space Complexity: O(target)
    """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]
