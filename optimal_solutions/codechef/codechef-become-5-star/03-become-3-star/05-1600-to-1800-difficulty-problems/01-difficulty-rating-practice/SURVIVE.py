# cook your dish here
from math import ceil


def solve():
    for _ in range(int(input())):
        n,day,tot = map(int,input().split())
        if tot >= 7 and 6*(n-day) < day:
            print(-1)
        else:
            print(ceil((tot*day)/n))


if __name__ == "__main__":
    solve()
