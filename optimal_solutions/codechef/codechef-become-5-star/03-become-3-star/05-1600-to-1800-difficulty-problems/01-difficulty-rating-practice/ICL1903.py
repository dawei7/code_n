import math
import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        candies, friends, batch = data[idx:idx + 3]
        idx += 3
        limit = candies - friends
        g = math.gcd(batch, friends)
        if limit < 0 or candies % g:
            out.append('-1')
            continue
        mod = friends // g
        if mod == 1:
            throws = 0
        else:
            throws = candies // g * pow(batch // g, -1, mod) % mod
        out.append(str(throws if throws * batch <= limit else -1))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
