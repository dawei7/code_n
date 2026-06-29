


def solve():
    for _ in range(int(input())):
        n, x, y = map(int, input().split())
        print('Yes' if n <= x*y else 'No')


if __name__ == "__main__":
    solve()
