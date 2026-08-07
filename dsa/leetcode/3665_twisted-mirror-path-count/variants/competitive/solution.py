# Time:  O(m * n)
# Space: O(min(m, n))

# dp
class Solution:
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        def get(r, c):
            return grid[r][c] if len(grid) > len(grid[0]) else grid[c][r]

        dp = [[0]*2 for _ in range(min(len(grid), len(grid[0]))+1)]
        dp[1] = [1]*2
        for r in range(max(len(grid), len(grid[0]))):
            for c in range(len(dp)-1):
                if get(r, c):
                    dp[c+1] = [dp[c+1][1], dp[c][0]]
                else:
                    dp[c+1] = [(dp[c+1][1]+dp[c][0])%MOD]*2
        return dp[-1][0]


# Time:  O(m * n)
# Space: O(n)
# dp
class Solution2(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        dp = [[0]*2 for _ in range(len(grid[0])+1)]
        dp[1] = [1]*2
        for r in range(len(grid)):
            for c in range(len(dp)-1):
                if grid[r][c]:
                    dp[c+1] = [dp[c+1][1], dp[c][0]]
                else:
                    dp[c+1] = [(dp[c+1][1]+dp[c][0])%MOD]*2
        return dp[-1][0]
