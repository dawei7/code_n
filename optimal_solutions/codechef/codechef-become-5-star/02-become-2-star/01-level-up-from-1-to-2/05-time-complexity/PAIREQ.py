# cook your dish here
from statistics import mode


def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        m = mode(a)
        print(len(a)-(a.count(m)))


if __name__ == "__main__":
    solve()
