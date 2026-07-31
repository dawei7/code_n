from math import gcd


def solve(n, a, b):
    modulus = 1_000_000_007
    least_common_multiple = a // gcd(a, b) * b
    low = 1
    high = n * min(a, b)

    while low < high:
        middle = (low + high) // 2
        count = middle // a + middle // b - middle // least_common_multiple
        if count >= n:
            high = middle
        else:
            low = middle + 1

    return low % modulus
