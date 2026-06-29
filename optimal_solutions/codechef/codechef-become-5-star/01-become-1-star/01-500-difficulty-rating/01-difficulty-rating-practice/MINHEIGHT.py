


def solve():
    t = int(input())
    for _ in range(t):
        x, h = map(int, input().split())
        if x >= h:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
