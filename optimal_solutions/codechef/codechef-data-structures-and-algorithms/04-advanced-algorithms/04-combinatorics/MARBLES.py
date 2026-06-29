import math


def solve():
    t = int(input())
    while t>0:
        n,k = map(int,input().split())
        print(math.comb(n-1,k-1))
        t -= 1


if __name__ == "__main__":
    solve()
