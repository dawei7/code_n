


def solve():
    for _ in range(int(input())):
        X, Y = map(int, input().split())
        exp = Y * 30
        if X >= exp:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
