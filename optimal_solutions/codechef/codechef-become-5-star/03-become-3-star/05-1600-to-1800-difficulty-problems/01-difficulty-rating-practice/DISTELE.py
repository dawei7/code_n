# www.codechef.com/problems/DISTELE

from sys import stdin
from collections import Counter


def solve():
    def count_subsets():
        N = int(stdin.readline())
        freqs = Counter(map(int, stdin.readline().split()))
        subsets = 1
        for opt in freqs.values():
            subsets *= opt + 1
            subsets %= 1000000007

        return subsets - 1 # remove empty set 
        #(fortunately we cannot arrive at 0 by modulo ops, as 1000000007 is prime)


    # ======================= #

    if __name__ == "__main__":
        T = int(input())
        for _ in range(T):
            print(count_subsets())


if __name__ == "__main__":
    solve()
