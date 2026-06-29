import sys
import math

def possible(x):
    target = x + 4
    limit = math.isqrt(target)
    for divisor in range(3, limit + 1):
        if target % divisor == 0 and target // divisor >= 3:
            return True
    return False

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = ['YES' if possible(x) else 'NO' for x in data[1:1 + t]]
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
