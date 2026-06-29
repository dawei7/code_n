


def solve():
    t = int(input())
    for _ in range(t):
        f, s = map(int, input().split())
        if f < s:
            print("FIRST")
        elif f > s:
            print("SECOND")
        else:
            print("ANY")


if __name__ == "__main__":
    solve()
