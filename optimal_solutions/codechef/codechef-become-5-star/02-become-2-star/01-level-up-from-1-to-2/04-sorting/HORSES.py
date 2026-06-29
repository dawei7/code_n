


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        s.sort()

        minval = float('inf')
        for i in range(1, n):
            minval = min(minval, s[i] - s[i - 1])
        print(minval)


if __name__ == "__main__":
    solve()
