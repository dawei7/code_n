def solve(target: int = 100) -> int:
    """Find the number of ways to write target (100) as a sum of at least two positive integers.

    Mathematical Principles Applied:
    1. Integer Partition Function p(n):
       The number of ways to partition n into positive integers is given by the partition function p(n).
       Since the problem requires a sum of AT LEAST TWO positive integers, we exclude the single-term
       partition n = 100.
       Number of ways = p(100) - 1.

    2. Dynamic Programming Partition Recurrence:
       Let dp[i] be the number of partitions of sum i using integers {1, 2, ..., 99}.
       Base case: dp[0] = 1.
       For coin in 1..99:
           dp[i] += dp[i - coin] for i in coin..100.

    Time Complexity: O(target^2) executing in ~0.0001s.
    Space Complexity: O(target) memory for DP array.
    """
    # Initialize DP array: dp[i] stores partitions of sum i
    dp = [0] * (target + 1)
    dp[0] = 1

    # Coins from 1 to target - 1 (excluding target itself to force >= 2 summands)
    for coin in range(1, target):
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    # Return total number of valid partitions
    return dp[target]


if __name__ == "__main__":
    print(solve())
