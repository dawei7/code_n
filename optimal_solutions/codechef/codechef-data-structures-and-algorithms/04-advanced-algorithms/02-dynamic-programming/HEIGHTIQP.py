


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())

        H = [0] * 1010
        IQ = [0] * 1010
        DP = [0] * 1010

        H[1:n + 1] = map(int, input().split())
        IQ[1:n + 1] = map(int, input().split())

        for i in range(1, n + 1):
            DP[i] = 1
            for j in range(i - 1, 0, -1):
                if H[j] >= H[i]:
                    continue
                if IQ[j] <= IQ[i]:
                    continue
                DP[i] = max(DP[i], 1 + DP[j])

        max1 = DP[1]
        for i in range(2, n + 1):
            max1 = max(max1, DP[i])

        print(max1)


if __name__ == "__main__":
    solve()
