


def solve():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        print(min(a + b, c + d))


if __name__ == "__main__":
    solve()
