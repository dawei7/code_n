


def solve():
    t = int(input())
    for _ in range(t):
        n, m, h = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        a.sort(reverse=True)
        b.sort(reverse=True)

        total = 0
        for i in range(min(n, m)):
            total += min(a[i], b[i] * h)

        print(total)


if __name__ == "__main__":
    solve()
