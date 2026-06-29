import sys


def solve():
    input = sys.stdin.readline
    _ = int(input())
    while _:
        _ -= 1
        ans = []
        d = int(input())
        lim = 100000
        while d >= lim - 1:
            ans += [lim, lim - 1, 1]
            d -= (lim - 2)
        ans += [d + 1, d + 2]
        print(len(ans))
        print(*ans)


if __name__ == "__main__":
    solve()
