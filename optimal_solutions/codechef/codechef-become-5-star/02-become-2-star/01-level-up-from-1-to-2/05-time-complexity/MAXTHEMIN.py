


def solve():
    t=int(input())
    for i in range(t):
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        a.sort()
        if k<=n-1:
            print(a[k])
        else:
            print(a[n-1])


if __name__ == "__main__":
    solve()
