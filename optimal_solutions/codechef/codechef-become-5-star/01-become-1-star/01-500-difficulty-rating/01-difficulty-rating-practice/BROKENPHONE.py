


def solve():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        print('repair' if x < y else ('new phone' if x > y else 'any'))


if __name__ == "__main__":
    solve()
