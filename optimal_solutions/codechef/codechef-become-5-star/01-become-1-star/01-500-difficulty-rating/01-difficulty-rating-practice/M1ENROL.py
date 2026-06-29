


def solve():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        print(max(0, y - x))


if __name__ == "__main__":
    solve()
