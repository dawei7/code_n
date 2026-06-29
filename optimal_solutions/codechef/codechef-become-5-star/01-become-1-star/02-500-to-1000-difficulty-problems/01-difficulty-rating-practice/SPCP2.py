


def solve():
    for i in range(int(input())):
        x,n=map(int,input().split())
        a=(n // 100) + (1 if n % 100 != 0 else 0)
        b=max(0,a-x)
        print(b)


if __name__ == "__main__":
    solve()
