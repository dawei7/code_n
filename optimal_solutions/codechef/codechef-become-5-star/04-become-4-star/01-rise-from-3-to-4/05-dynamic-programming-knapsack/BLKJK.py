


def solve():
    left = [[0] * 1024 for _ in range(1024)]
    right = [[0] * 1024 for _ in range(1024)]

    def solveCase(N, X, Y, a):
        for i in range(N + 2):
            left[0][i] = right[0][i] = 0

        left[0][0] = 1
        right[0][N] = (1 << (Y + 1)) - (1 << X)
        max_mask = (1 << (Y + 1)) - 1

        for missed in range(N // 2 + 1):
            left[missed + 1][0] = 0
            for i in range(N):
                left[missed][i + 1] |= (left[missed][i] << a[i]) & max_mask
                left[missed + 1][i + 1] = left[missed][i]

            right[missed + 1][N] = 0
            for i in range(N, 0, -1):
                right[missed + 1][i - 1] = right[missed][i] >> a[i - 1]
                right[missed][i - 1] |= right[missed][i]

            if any(right[missed][i] & left[missed][i] for i in range(1, N + 1)):
                return missed

        return -1

    T = int(input())
    for _ in range(T):
        N, X, Y = map(int, input().split())
        a = list(map(int, input().split()))
        print(solveCase(N, X, Y, a))


if __name__ == "__main__":
    solve()
