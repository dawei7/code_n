


def solve():
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        print('Yes' if a+b == c else 'No')


if __name__ == "__main__":
    solve()
