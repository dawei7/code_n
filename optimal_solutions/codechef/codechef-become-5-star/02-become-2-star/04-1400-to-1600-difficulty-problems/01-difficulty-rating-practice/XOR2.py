import sys
from functools import reduce
from operator import xor

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = data[idx:idx + n]
        idx += n
        total = reduce(xor, values, 0)
        out.append('YES' if n % 2 == 1 or total == 0 else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
