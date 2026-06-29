import functools
import math


def solve():
    def primes_dividing(a):
        rv = []
        while sieve[a] not in [0, None]:
            p = sieve[a]
            a //= p
            rv.append(p)
        if sieve[a] is None:
            rv.append(a)
        return rv

    def LII():
        return [int(x) for x in input().split()]

    s_size = 10 ** 6 + 1
    sieve = [0, 0] + [None] * (s_size - 2)
    for i in range(2, math.isqrt(s_size - 1) + 1):
        if sieve[i] is None:
            for j in range(i * i, s_size, i):
                sieve[j] = i

    primes = [i for i in range(s_size) if sieve[i] is None]

    for _ in range(int(input())):
        n, m = LII()
        a = LII()
        assert len(a) == n
        gcd_a = functools.reduce(math.gcd, a)
        if all(x == gcd_a for x in a):
            print(0)
            continue
        if gcd_a > 1:
            print(1)
            print(gcd_a)
            continue
        all_primes = set(x for y in a for x in primes_dividing(y))
        d = 0
        for p in primes:
            if p > m:
                break
            if p not in all_primes:
                d = p
                break
        if d == 0:
            print(2)
            print(2)
            print(3)
        else:
            print(1)
            print(d)


if __name__ == "__main__":
    solve()
