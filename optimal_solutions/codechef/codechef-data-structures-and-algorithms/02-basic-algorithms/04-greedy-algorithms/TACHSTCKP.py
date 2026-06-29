


def solve():
    n, d = map(int, input().split())
    a = sorted([int(input()) for _ in range(n)])

    pairs = 0

    i = 0
    while i < n - 1:
        if a[i + 1] - a[i] <= d:
            pairs += 1
            i += 2
        else:
            i += 1

    print(pairs)


if __name__ == "__main__":
    solve()
