# cook your dish here


def solve():
    t=int(input())
    while t>0:
        a,b=map(int,input().split())
        print(a//(2*b))
        t-=1


if __name__ == "__main__":
    solve()
