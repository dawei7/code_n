# cook your dish here


def solve():
    t=int(input())
    for _ in range(t):
        l,r=map(int,input().split())
        if l>=(r-l+1):
            print(r)
        else:
            print(-1)


if __name__ == "__main__":
    solve()
