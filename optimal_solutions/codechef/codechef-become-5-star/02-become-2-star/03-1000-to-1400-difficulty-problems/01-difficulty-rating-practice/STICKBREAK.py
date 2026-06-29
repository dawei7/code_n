# cook your dish here


def solve():
    t = int(input())
    for _ in range(t):
        Length, Parts = map(int, input().split())
        if Length % Parts == 0:
            print(0)
        else:
            print(1)


if __name__ == "__main__":
    solve()
