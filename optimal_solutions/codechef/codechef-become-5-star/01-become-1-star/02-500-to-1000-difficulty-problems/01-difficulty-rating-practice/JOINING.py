# cook your dish here
import math


def solve():
    for i in range(int(input())):
        a,b=map(int,input().split())
        print(math.ceil(a/5)-math.ceil(b/5))


if __name__ == "__main__":
    solve()
