def solve(target: int = 200) -> int:
    """Find the number of ways to make target pence (200p = 2 pounds) using UK coins.

    Mathematical Principles Applied:
    1. Unbounded Knapsack / Coin Change DP (Generating Functions):
       Let C = {1, 2, 5, 10, 20, 50, 100, 200} be the coin denominations.
       The generating function for the number of ways is:
       G(x) = prod_{c in C} 1 / (1 - x^c)

    2. In-Place Dynamic Programming Recurrence:
       Let dp[i] be the number of ways to make sum i.
       Base case: dp[0] = 1 (1 way to make 0p).
       For each coin c in C, update for i from c to target:
       dp[i] = dp[i] + dp[i - c]

    Time Complexity: O(|C| * target) where |C| = 8 and target = 200 (1,600 ops).
    Space Complexity: O(target) memory for DP array.
    """
    # UK coin denominations in pence
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    # Initialize DP array: dp[i] stores number of combinations to make sum i
    dp = [0] * (target + 1)
    dp[0] = 1

    # Outer loop over coin denominations (prevents permutation duplicates)
    for coin in coins:
        # Inner loop over target sums from coin value up to target
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    # Return total number of combinations to make target amount
    return dp[target]


if __name__ == "__main__":
    print(solve())
