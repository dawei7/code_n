# cook your dish here


def solve():
    t=int(input())
    for i in range(t):
        n,m=map(int, input().split())
        a=list(map(int,input().split()))
        b=set(a)
        if len(b)<m:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
