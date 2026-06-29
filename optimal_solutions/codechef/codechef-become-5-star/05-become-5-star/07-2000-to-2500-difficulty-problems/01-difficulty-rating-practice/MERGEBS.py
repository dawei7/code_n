# cook your dish here
# cook your dish here


def solve():
    for i in range(int(input())):
        N = int(input())
        A = input()
        B = input()
        sufA = [0]
        sufB = [0]
        for i in range(N - 1, -1, -1):
            if A[i] == "0":
                sufA.append(sufA[-1] + 1)
            else:
                sufA.append(sufA[-1])

            if B[i] == "0":
                sufB.append(sufB[-1] + 1)
            else:
                sufB.append(sufB[-1])

        sufB.reverse()
        sufA.reverse()
        dp = []

        from math import inf
        for i in range(N + 1):
            dp.append([inf] * (N + 1))
        dp[0][0] = 0
        for j in range(N + 1):
            for i in range(N + 1):
                if j < N:
                    if B[j] == "0":
                        dp[i][j + 1] = min(dp[i][j + 1], dp[i][j])
                    else:
                        dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + sufA[i] + sufB[j])

                if i < N:
                    if A[i] == "0":
                        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
                    else:
                        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + sufA[i] + sufB[j])

        print(dp[N][N])


if __name__ == "__main__":
    solve()
