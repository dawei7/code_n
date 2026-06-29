# cook your dish here


def solve():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        print((a[-1]-a[0])*2)


if __name__ == "__main__":
    solve()
