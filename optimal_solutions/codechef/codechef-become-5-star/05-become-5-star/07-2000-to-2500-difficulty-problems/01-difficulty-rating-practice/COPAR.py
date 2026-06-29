# cook your dish here
import sys


def solve():
    input = sys.stdin.read
    sys.setrecursionlimit(10**5)

    N = 100000 + 9
    spf = [0] * N

    for i in range(1, N):
        spf[i] = i
    for i in range(2, N):
        j = i
        while j < N:
            spf[j] = min(spf[j], i)
            j += i

    data = input().split()
    t = int(data[0])
    idx = 1

    while t > 0:
        t -= 1
        n = int(data[idx])
        idx += 1
        a = [0] * (n + 1)
        for i in range(1, n + 1):
            a[i] = int(data[idx])
            idx += 1

        rgt = []
        for i in range(1, n + 1):
            x = a[i]
            while x > 1:
                p = spf[x]
                while x % p == 0:
                    rgt.append(p)
                    x //= p

        lft = set()
        rgt_multiset = dict()
        for x in rgt:
            if x in rgt_multiset:
                rgt_multiset[x] += 1
            else:
                rgt_multiset[x] = 1

        for i in range(1, n + 1):
            x = a[i]
            while x > 1:
                p = spf[x]
                while x % p == 0:
                    if rgt_multiset[p] == 1:
                        del rgt_multiset[p]
                    else:
                        rgt_multiset[p] -= 1
                    lft.add(p)
                    x //= p

            found = True
            for p in lft:
                if p in rgt_multiset:
                    found = False
                    break

            if found:
                print(i)
                break


if __name__ == "__main__":
    solve()
