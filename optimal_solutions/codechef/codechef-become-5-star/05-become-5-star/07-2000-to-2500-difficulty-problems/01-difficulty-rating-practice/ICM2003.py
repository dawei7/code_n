# cook your dish here
from math import pi,sin


def solve():
    for _ in range(int(input())):

        b,c=map(float,input().split())
        f=lambda x:(x**2 + b*x +c)/sin(x)
        l,r,err=0,pi/2,1e-7
        while r-l>err:
            m1=l+(r-l)/3
            m2=r-(r-l)/3
            f1,f2=f(m1),f(m2)
            if f1>f2:
                l=m1
            else:
                r=m2
        print(f(l))


if __name__ == "__main__":
    solve()
