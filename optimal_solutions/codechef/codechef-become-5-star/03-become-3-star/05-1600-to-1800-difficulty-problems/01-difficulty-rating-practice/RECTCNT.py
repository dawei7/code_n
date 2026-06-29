import sys
from collections import Counter, defaultdict

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    out = []
    while idx < len(data):
        n = data[idx]
        idx += 1
        if n == 0:
            break
        by_x = defaultdict(list)
        for _ in range(n):
            x, y = (data[idx], data[idx + 1])
            idx += 2
            by_x[x].append(y)
        pairs = Counter((tuple(sorted(ys)) for ys in by_x.values() if len(ys) == 2))
        out.append(str(sum((count * (count - 1) // 2 for count in pairs.values()))))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
