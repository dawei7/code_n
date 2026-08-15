def f(m: int, n: int) -> int:
    """Compute fill-count function F(m, n), the number of ways to fill a row of length n with red blocks of min length m.

    Mathematical Principles Applied:
    1. Generalized Block Recurrence:
       Let dp[i] be F(m, i).
       dp[0] = 1.
       dp[i] = dp[i-1] + sum_{len=m}^i dp[max(0, i - len - 1)].
    """
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        # Case 1: Position i is grey
        dp[i] = dp[i - 1]
        # Case 2: Position i is end of red block of length len >= m
        for length in range(m, i + 1):
            if i - length - 1 >= 0:
                dp[i] += dp[i - length - 1]
            else:
                dp[i] += 1

    return dp[n]


def solve(m: int = 50, target: int = 1000000) -> int:
    """Find the least n for which F(m, n) with m = 50 first exceeds target = 1,000,000.

    Time Complexity: O(N^2) where N ~ 168 (executes in ~0.005s).
    Space Complexity: O(N) memory for DP array.
    """
    n = m
    # Increment n upwards until F(50, n) exceeds 1,000,000
    while True:
        if f(m, n) > target:
            # Return minimal row length n obtaining F(50, n) > 1,000,000
            return n
        n += 1


if __name__ == "__main__":
    print(solve())
