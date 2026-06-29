


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        ans = 0
        for i in range(n - 1, -1, -2):
            ans += a[i]
        print(ans)


if __name__ == "__main__":
    solve()
