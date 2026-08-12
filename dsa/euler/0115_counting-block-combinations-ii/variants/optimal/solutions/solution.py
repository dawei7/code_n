def f(m: int, n: int) -> int:
    """Compute fill-count function F(m, n)."""
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        for length in range(m, i + 1):
            if i - length - 1 >= 0:
                dp[i] += dp[i - length - 1]
            else:
                dp[i] += 1

    return dp[n]


def solve(m: int = 50, target: int = 1000000) -> int:
    """Find least n for which F(m, n) first exceeds target.
    
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    n = m
    while True:
        if f(m, n) > target:
            return n
        n += 1
