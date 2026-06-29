import math


def solve():
    for _ in range(int(input())):
        x,y=map(int,input().split())
        s=2*(x-y)
        print(round(math.sqrt(s)))


if __name__ == "__main__":
    solve()
