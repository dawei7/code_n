# cook your dish here


def solve():
    t=int(input())
    while(t>0):
        a,b,c,d=map(int,input().split())
        e=abs(a-c)
        f=abs(b-d)
        print(max(e,f))
        t-=1


if __name__ == "__main__":
    solve()
