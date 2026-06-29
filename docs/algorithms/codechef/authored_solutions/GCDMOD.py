import math
import sys


MOD = 1000000007


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        a, b, n = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        diff = abs(a - b)
        if diff == 0:
            out.append(str((pow(a, n, MOD) + pow(b, n, MOD)) % MOD))
        else:
            value = (pow(a, n, diff) + pow(b, n, diff)) % diff
            out.append(str(math.gcd(value, diff) % MOD))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
