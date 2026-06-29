# cook your dish here
import math


def solve():
    t=int(input())
    for i in range(t):
        n,x=map(int,input().split())
        n=math.ceil(n/6)
        print(n*x)


if __name__ == "__main__":
    solve()
