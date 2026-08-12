import math


def solve(max_n: int = 10000) -> int:
    """Find sum of D(N) for 5 <= N <= max_n.
    
    Time Complexity: O(max_n * log(max_n))
    Space Complexity: O(1)
    """
    E = math.e
    total = 0

    for N in range(5, max_n + 1):
        k1 = int(N / E)
        k2 = k1 + 1

        if k1 * math.log(N / k1) > k2 * math.log(N / k2):
            k = k1
        else:
            k = k2

        d = k // math.gcd(N, k)
        while d % 2 == 0:
            d //= 2
        while d % 5 == 0:
            d //= 5

        if d == 1:
            total -= N
        else:
            total += N

    return total
