


def solve():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        if y > x:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    solve()
