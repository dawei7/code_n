from math import *


def solve():
    for _ in range(int(input())):
        n = int(input())
        t = int(isqrt(n))
        x = t
        print((x >> 1) + (x & n & 1))


if __name__ == "__main__":
    solve()
