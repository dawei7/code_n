# cook your dish here
# https://docs.python.org/3/library/collections.html
from collections import *

# https://docs.python.org/3/library/math.html
from math import ceil, floor, fsum, gcd, lcm, factorial, perm, comb, log, log2, log10, pow, sqrt


def solve():
    def inp():
        return input().rstrip()

    def intinp():
        return int(input().rstrip())

    def mapintinp():
        return map(int, input().split())

    def lstintinp():
        return list(map(int, input().split()))

    def lstinp():
        return list(input().split())

    def total(iterable):
        return int(fsum(iterable))

    from statistics import mode
    for _ in range(intinp()):
        n = intinp()

        A = lstintinp()

        c = mode(A)
        m = A.count(c)
        # print(c)
        if n<=2:
            print(0)
        else:
            if (m==1):
                print(n-2)
            else:
                print(n-m)


if __name__ == "__main__":
    solve()
