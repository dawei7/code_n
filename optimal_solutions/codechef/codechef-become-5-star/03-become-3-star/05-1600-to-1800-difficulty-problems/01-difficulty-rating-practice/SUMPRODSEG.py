# cook your dish here
import math


def solve():
    def minn(n):
       root=int(n**0.5)
       for i in range(root,0,-1):
            if n%i==0:
             return i,n//i
    for tc in range(int(input())):
        s,m=map(int,input().split())
        xs=s//2
        ys=s-xs
        xm,ym=minn(m)
        if xm>ys or xs>ym:

            print(xm,ym)
            print(xs,ys)
        else:
            print(-1)


if __name__ == "__main__":
    solve()
