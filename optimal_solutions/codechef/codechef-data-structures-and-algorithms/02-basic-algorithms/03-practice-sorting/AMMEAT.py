


def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        p = list(map(int, input().split()))

        p.sort(reverse=True)

        tot = 0
        d = 0

        for i in range(n):
            tot += p[i]
            if tot >= m:
                d = i + 1
                break

        if d == 0:
            print(-1)
        else:
            print(d)


if __name__ == "__main__":
    solve()
