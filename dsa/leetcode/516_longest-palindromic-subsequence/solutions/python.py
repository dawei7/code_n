"""Space-compressed interval DP for LeetCode 516."""


def solve(s: str) -> int:
    size = len(s)
    dp = [0] * size
    for left in range(size - 1, -1, -1):
        dp[left] = 1
        diagonal = 0
        for right in range(left + 1, size):
            previous_row = dp[right]
            if s[left] == s[right]:
                dp[right] = diagonal + 2
            else:
                dp[right] = max(dp[right], dp[right - 1])
            diagonal = previous_row
    return dp[-1]
