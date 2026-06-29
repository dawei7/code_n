


def solve():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        print(max(0, n - m))


if __name__ == "__main__":
    solve()
