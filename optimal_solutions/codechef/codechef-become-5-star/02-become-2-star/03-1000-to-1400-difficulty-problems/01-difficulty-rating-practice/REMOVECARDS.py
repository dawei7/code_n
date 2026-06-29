# cook your dish here
from statistics import mode


def solve():
    for _ in range(int(input())):
        n = int(input())
        k = list(map(int,input().split()))
        j = mode(k)
        cn = k.count(j)
        print(n-cn)


if __name__ == "__main__":
    solve()
