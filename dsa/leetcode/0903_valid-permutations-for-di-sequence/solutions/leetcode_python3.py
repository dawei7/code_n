class Solution:
    def numPermsDISequence(self, s: str) -> int:
        modulo = 1_000_000_007
        dp = [1] * (len(s) + 1)

        for relation in s:
            if relation == "I":
                next_dp = []
                running = 0
                for value in dp[:-1]:
                    running = (running + value) % modulo
                    next_dp.append(running)
            else:
                next_dp = [0] * (len(dp) - 1)
                running = 0
                for index in range(len(dp) - 1, 0, -1):
                    running = (running + dp[index]) % modulo
                    next_dp[index - 1] = running
            dp = next_dp

        return dp[0]
