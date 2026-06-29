


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        A = [[0] * 101 for _ in range(101)]
        DP = [[0] * 101 for _ in range(101)]

        for i in range(1, n + 1):
            A[i][1:n + 1] = map(int, input().split())

        DP[1][1] = A[1][1]
        for i in range(2, n + 1):
            DP[1][i] = DP[1][i - 1] + A[1][i]
        for i in range(2, n + 1):
            DP[i][1] = DP[i - 1][1] + A[i][1]
            for j in range(2, n + 1):
                DP[i][j] = A[i][j] + max(DP[i - 1][j], DP[i][j - 1])

        if DP[n][n] < 0:
            print("Bad Judges")
        else:
            print(f"{DP[n][n] / (2 * n - 3):.9f}")


if __name__ == "__main__":
    solve()
