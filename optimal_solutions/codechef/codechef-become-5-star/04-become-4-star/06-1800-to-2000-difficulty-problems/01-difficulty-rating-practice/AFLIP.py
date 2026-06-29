import sys
from collections import Counter

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, m = (data[idx], data[idx + 1])
        idx += 2
        total = n * m
        a = data[idx:idx + total]
        idx += total
        b = data[idx:idx + total]
        idx += total
        if n == 1 or m == 1:
            out.append('Yes' if a == b else 'No')
            continue
        a_groups = [Counter(), Counter()]
        b_groups = [Counter(), Counter()]
        for i in range(n):
            base = i * m
            for j in range(m):
                parity = i + j & 1
                a_groups[parity][a[base + j]] += 1
                b_groups[parity][b[base + j]] += 1
        out.append('Yes' if a_groups == b_groups else 'No')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
