import math
import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        a, b = (data[idx], data[idx + 1])
        idx += 2
        while b > 1:
            g = math.gcd(a, b)
            if g == 1:
                break
            while b % g == 0:
                b //= g
        out.append('Yes' if b == 1 else 'No')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
