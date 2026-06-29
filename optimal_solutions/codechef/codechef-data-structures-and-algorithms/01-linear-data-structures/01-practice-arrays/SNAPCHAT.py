


def solve():
    t = int(input())

    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        ans, cur = 0, 0
        for i in range(n):
            if a[i] > 0 and b[i] > 0: cur += 1
            else: cur = 0
            ans = max(ans, cur)
        print(ans)
        t -= 1


if __name__ == "__main__":
    solve()
