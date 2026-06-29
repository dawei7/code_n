


def solve():
    for _ in range(int(input())):
        n, x = map(int, input().split())
        print('Yes' if 2*x >= n else 'No')


if __name__ == "__main__":
    solve()
