# cook your dish here


def solve():
    t=eval(input())
    while(t>0):
        x,y,z=map(eval,input().split())
        print((z*x)-(y*x))
        t-=1


if __name__ == "__main__":
    solve()
