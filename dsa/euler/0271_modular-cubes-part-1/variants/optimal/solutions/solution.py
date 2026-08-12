import itertools
from functools import reduce


def solve() -> int:
    """Find S(13082761331670030), the sum of all 1 < x < N for which x^3 = 1 (mod N).
    
    Time Complexity: O(3^k) CRT combinations for k primes = 1 (mod 3)
    Space Complexity: O(3^k)
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    N = reduce(lambda a, b: a * b, primes)

    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        return gcd, y1 - (b // a) * x1, x1

    crt_info = []
    for p in primes:
        roots = [x for x in range(p) if (x * x * x) % p == 1]
        M_i = N // p
        _, inv, _ = extended_gcd(M_i, p)
        crt_info.append((p, roots, M_i, inv % p))

    ans = 0
    for choice in itertools.product(*[info[1] for info in crt_info]):
        x = 0
        for i in range(len(primes)):
            _, _, M_i, inv = crt_info[i]
            x = (x + choice[i] * M_i * inv) % N
        if x > 1:
            ans += x

    return ans
