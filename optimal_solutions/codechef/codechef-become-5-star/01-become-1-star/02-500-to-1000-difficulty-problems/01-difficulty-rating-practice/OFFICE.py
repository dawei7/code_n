# cook your dish here


def solve():
    T=int(input())
    for i in range(1,T+1):
       x,y=map(int,input().split())
       a=4*x
       b=y
       print(a+b)


if __name__ == "__main__":
    solve()
