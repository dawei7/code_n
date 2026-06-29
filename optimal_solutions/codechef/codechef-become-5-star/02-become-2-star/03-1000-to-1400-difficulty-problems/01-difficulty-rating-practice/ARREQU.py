import sys
from collections import Counter

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
        max_frequency = max(Counter(values).values())
        out.append('YES' if max_frequency <= (n + 1) // 2 else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
