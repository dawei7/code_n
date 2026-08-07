from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        for row_index in range(len(triangle) - 2, -1, -1):
            for column, value in enumerate(triangle[row_index]):
                dp[column] = value + min(dp[column], dp[column + 1])
        return dp[0]
