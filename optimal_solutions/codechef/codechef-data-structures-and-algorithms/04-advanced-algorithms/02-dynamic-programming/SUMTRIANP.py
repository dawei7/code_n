


def solve():
    T = int(input())

    for _ in range(T):
        n = int(input())

        DP = [[0] * 101 for _ in range(101)]
        A = [[0] * 101 for _ in range(101)]

        for i in range(1, n + 1):
            row = list(map(int, input().split()))
            for j in range(1, i + 1):
                A[i][j] = row[j - 1]
                if j == 1:
                    DP[i][j] = A[i][j] + DP[i - 1][j]
                else:
                    DP[i][j] = A[i][j] + max(DP[i - 1][j - 1], DP[i - 1][j])

        ans = DP[n][1]
        for i in range(2, n + 1):
            ans = max(ans, DP[n][i])

        print(ans)


if __name__ == "__main__":
    solve()
