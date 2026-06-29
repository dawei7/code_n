import sys
from collections import Counter

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, x = (data[idx], data[idx + 1])
        idx += 2
        values = data[idx:idx + n]
        idx += n
        freq = Counter(values)
        best_count = -1
        best_ops = 10 ** 18
        for value, count in freq.items():
            if x == 0:
                total, ops = (count, 0)
            else:
                total, ops = (count + freq.get(value ^ x, 0), freq.get(value ^ x, 0))
            if total > best_count or (total == best_count and ops < best_ops):
                best_count, best_ops = (total, ops)
        out.append(f'{best_count} {best_ops}')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
