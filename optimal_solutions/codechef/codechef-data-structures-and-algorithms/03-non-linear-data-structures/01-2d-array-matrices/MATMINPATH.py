


def solve():
    def minPathSum(mat):
        m = len(mat)
        n = len(mat[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = mat[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + mat[i][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + mat[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + mat[i][j]

        return dp[m - 1][n - 1]

    if __name__ == "__main__":
        n, m = map(int, input().split())

        assert 1 <= n <= 100
        assert 1 <= m <= 100

        mat = [list(map(int, input().split())) for _ in range(n)]

        print(minPathSum(mat))


if __name__ == "__main__":
    solve()
