


def solve():
    a, b, x, y = map(int, input().split())
    messi = 2*a + b
    ronaldo = 2*x + y
    print('Messi' if messi > ronaldo else ('Ronaldo' if messi < ronaldo else 'Equal'))


if __name__ == "__main__":
    solve()
