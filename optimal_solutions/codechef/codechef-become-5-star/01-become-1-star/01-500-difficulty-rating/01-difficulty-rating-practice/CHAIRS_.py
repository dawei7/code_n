


def solve():
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split())
        print(max(x - y, 0))


if __name__ == "__main__":
    solve()
