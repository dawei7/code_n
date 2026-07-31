class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[1] * (k + 1) for _ in range(n)]

        for left in range(n - 2, -1, -1):
            diagonal = [0] * (k + 1)
            for right in range(left + 1, n):
                without_left = dp[right]
                without_right = dp[right - 1]
                current = [0] * (k + 1)

                difference = abs(ord(s[left]) - ord(s[right]))
                pair_cost = min(difference, 26 - difference)

                for budget in range(k + 1):
                    best = max(without_left[budget], without_right[budget])
                    if pair_cost <= budget:
                        best = max(best, diagonal[budget - pair_cost] + 2)
                    current[budget] = best

                diagonal = without_left
                dp[right] = current

        return dp[n - 1][k]
