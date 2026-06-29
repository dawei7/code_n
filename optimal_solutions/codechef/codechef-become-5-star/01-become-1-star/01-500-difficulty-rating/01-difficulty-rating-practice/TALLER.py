


def solve():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        if x > y:
            print("A")
        else:
            print("B")


if __name__ == "__main__":
    solve()
