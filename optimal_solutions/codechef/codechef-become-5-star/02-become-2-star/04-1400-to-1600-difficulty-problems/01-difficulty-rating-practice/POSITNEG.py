# cook your dish here
import sys
import calendar


def solve():
    for _ in range(int(input())):
        n=int(input())
        b=list(map(int,input().split()))
        o=b.count(-1)
        for i in range(n):
            if(b[i]==-1):
                o+=i
        q=(n*(n+1))
        s=q//2
        r=s-o
        print(abs(r-o))


if __name__ == "__main__":
    solve()
