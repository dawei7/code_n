import math
import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, first, kth = data[idx:idx + 3]
        idx += 3
        total = 180 * (n - 2)
        numerator = first * n * (n - 1) + (kth - 1) * (2 * (total - n * first))
        denominator = n * (n - 1)
        g = math.gcd(numerator, denominator)
        out.append(f'{numerator // g} {denominator // g}')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
