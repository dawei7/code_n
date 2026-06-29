# cook your dish here
from collections import Counter
from math import comb


def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        myDict = Counter(a)
        result = 0
        for value in myDict.values():
            result += comb(value, 2)
        print(result)


if __name__ == "__main__":
    solve()
