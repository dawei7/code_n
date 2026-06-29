


def solve():
    for _ in range(int(input())):
        a, b, c, d = map(int, input().split())
        if a-c < b-d:
            print('first')
        else:
            print('second' if a-c > b-d else 'any')


if __name__ == "__main__":
    solve()
