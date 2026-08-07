class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        infinity = n + 1
        dp = [[infinity] * (k + 1) for _ in range(n + 1)]
        for deletions in range(k + 1):
            dp[n][deletions] = 0

        for start in range(n - 1, -1, -1):
            for deletions in range(k + 1):
                if deletions > 0:
                    dp[start][deletions] = dp[start + 1][deletions - 1]

                kept = 0
                removed = 0
                for end in range(start, n):
                    if s[end] == s[start]:
                        kept += 1
                    else:
                        removed += 1
                    if removed > deletions:
                        break

                    encoded_length = 1
                    if kept >= 100:
                        encoded_length = 4
                    elif kept >= 10:
                        encoded_length = 3
                    elif kept >= 2:
                        encoded_length = 2
                    dp[start][deletions] = min(
                        dp[start][deletions],
                        encoded_length + dp[end + 1][deletions - removed],
                    )

        return dp[0][k]
