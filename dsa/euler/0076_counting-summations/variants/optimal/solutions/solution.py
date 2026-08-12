def solve(target: int = 100) -> int:
    """Find the number of ways to write target as a sum of at least two positive integers.
    
    Time Complexity: O(target^2)
    Space Complexity: O(target)
    """
    dp = [0] * (target + 1)
    dp[0] = 1

    # Coins from 1 to target - 1 (since we need at least 2 positive integers)
    for coin in range(1, target):
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]
