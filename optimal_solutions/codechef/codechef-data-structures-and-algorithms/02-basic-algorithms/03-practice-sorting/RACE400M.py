


def solve():
    t = int(input())
    for _ in range(t):
        x, y, z = map(int, input().split())
        if x == min(x, y, z): print('Alice')
        if y == min(x, y, z): print('Bob')
        if z == min(x, y, z): print('Charlie')


if __name__ == "__main__":
    solve()
