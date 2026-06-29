# cook your dish here
import bisect


def solve():
    primes = {2}
    primes = [False, False] + [True]*(10**6)
    p = 2
    dp = []
    while p*p <= (10**6):
        if primes[p] == True:
            for i in range(2*p, 10**6, p):
                primes[i] = False
        p += 1
    for i in range(2, i):
        if primes[i] and primes[i - 2]:
            dp.append(i)
    for _ in range(int(input())):
        print(bisect.bisect_right(dp, int(input())))


if __name__ == "__main__":
    solve()
