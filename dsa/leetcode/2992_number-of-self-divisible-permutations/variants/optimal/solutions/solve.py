from math import gcd


def solve(n: int) -> int:
    ways = [0] * (1 << n)
    ways[0] = 1

    for mask in range(1 << n):
        position = mask.bit_count() + 1
        for value in range(1, n + 1):
            bit = 1 << (value - 1)
            if mask & bit == 0 and gcd(value, position) == 1:
                ways[mask | bit] += ways[mask]

    return ways[-1]
