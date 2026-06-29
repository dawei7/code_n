# cook your dish here
from math import ceil


def solve():
    for i in range(int(input())):
        s,n = map(int,input().split())

        coin = 0
        if s%2!=0:
            coin = 1        #because at least 1 coin will be needed
            s-=1

        coin += ceil(s/n)

        print(coin)


if __name__ == "__main__":
    solve()
