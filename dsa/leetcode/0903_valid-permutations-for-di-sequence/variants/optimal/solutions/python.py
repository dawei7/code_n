"""Optimal app-local solution for LeetCode 903."""


MODULO = 1_000_000_007


def solve(s):
    dp = [1] * (len(s) + 1)
    for relation in s:
        next_dp = []
        if relation == "I":
            running = 0
            for value in dp[:-1]:
                running = (running + value) % MODULO
                next_dp.append(running)
        else:
            running = 0
            next_dp = [0] * (len(dp) - 1)
            for index in range(len(dp) - 1, 0, -1):
                running = (running + dp[index]) % MODULO
                next_dp[index - 1] = running
        dp = next_dp
    return dp[0]
