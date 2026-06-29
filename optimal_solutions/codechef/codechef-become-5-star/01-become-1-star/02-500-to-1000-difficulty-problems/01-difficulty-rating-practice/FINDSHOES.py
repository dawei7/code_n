


def solve():
    t = int(input())
    for i in range(t):
        n,m = map(int,input().split())

        if m>=n:
            print(n)
        else:
            print(n-m+n)


if __name__ == "__main__":
    solve()
