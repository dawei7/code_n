


def solve():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        print('Yes' if y >= 3*x else 'No')


if __name__ == "__main__":
    solve()
