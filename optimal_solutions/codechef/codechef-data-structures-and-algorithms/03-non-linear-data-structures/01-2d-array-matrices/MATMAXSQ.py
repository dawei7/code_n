


def solve():
    def maximalSquare(mat):
        m = len(mat)
        n = len(mat[0])

        maxside = 0
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or mat[i][j] == 0:
                    dp[i][j] = mat[i][j]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1]))

                maxside = max(maxside, dp[i][j])

        return maxside * maxside

    if __name__ == "__main__":
        n = int(input())

        assert 1 <= n <= 100

        mat = [list(map(int, input().split())) for _ in range(n)]
        for row in mat:
            assert all(x == 0 or x == 1 for x in row)

        print(maximalSquare(mat))


if __name__ == "__main__":
    solve()
