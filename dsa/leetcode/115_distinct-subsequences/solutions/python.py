def solve(s: str, t: str) -> int:
    if len(t) > len(s):
        return 0
    dp = [0] * (len(t) + 1)
    dp[0] = 1
    for source_character in s:
        for target_length in range(len(t), 0, -1):
            if source_character == t[target_length - 1]:
                dp[target_length] += dp[target_length - 1]
    return dp[-1]
