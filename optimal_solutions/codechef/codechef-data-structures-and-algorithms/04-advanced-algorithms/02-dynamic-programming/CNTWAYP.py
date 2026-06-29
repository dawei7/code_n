


def solve():
    t = int(input())

    N = 100002
    MOD = 10**9 + 7
    DP = [0] * N

    for _ in range(t):
        n, l = map(int, input().split())
        DP[0] = 1

        for i in range(1, n + 1):
            DP[i] = 0
            for j in range(i - 1, 0, -2):
                if i - j + 1 <= l:
                    DP[i] = (DP[i] + DP[j - 1]) % MOD

        print(DP[n])


if __name__ == "__main__":
    solve()
