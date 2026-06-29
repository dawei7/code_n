import math


def solve():
    for _ in range(int(input())):
        a,b,c,p,q,r=map(int,input().split())
        d=a+b+c
        a=p-a
        b=q-b
        c=r-c
        m=(p+q+r)/2
        if float(d+a)>m or float(d+b)>m or float(d+c)>m:print('YES')
        else:print('NO')


if __name__ == "__main__":
    solve()
