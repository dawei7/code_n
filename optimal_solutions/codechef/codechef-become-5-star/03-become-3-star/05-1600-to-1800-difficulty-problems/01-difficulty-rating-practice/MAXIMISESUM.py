


def solve():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))

        l = [0] * n
        r = [0] * n

        l[0] = arr[0]
        r[-1] = arr[-1]
        for i in range(1, n):
            l[i] = max(l[i - 1], arr[i])
            r[n - i - 1] = max(r[n - i], arr[n - i - 1])

        s = 0
        for i in range(n):
            s += min(l[i], r[i])
        print(s)


if __name__ == "__main__":
    solve()
