


def solve():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        print('Profit' if x < y else 'Loss' if x > y else 'Neutral')


if __name__ == "__main__":
    solve()
