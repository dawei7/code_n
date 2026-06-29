


def solve():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        print('Yes' if x > 10*y else 'No')


if __name__ == "__main__":
    solve()
