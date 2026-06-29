# cook your dish here
import math


def solve():
    def dis(x1,y1,x2,y2):
        d=((x1-x2)**2+(y1-y2)**2)
        return d

    sid=int(input())
    T = int(input())
    for tc in range(T):
        x1,y1,x2,y2,x3,y3= (map(int, input().split(' ')))
        d1=dis(x1,y1,x2,y2)
        d2=dis(x1,y1,x3,y3)
        d3=dis(x2,y2,x3,y3)
        t=""
        a=''
        M=max(d1,d2,d3)
        sumd=d1+d2+d3
        if d1!=d2 and d2!=d3 and d1!=d3:
            t="Scalene"
        else:
            t="Isosceles"
        if sid ==1:
            print(t,"triangle")
        elif sid==2:
            if M==sumd-M:
                a="right"
            elif M>sumd-M:
                a="obtuse"
            else:
                a='acute'
            print(t,a,"triangle")


if __name__ == "__main__":
    solve()
