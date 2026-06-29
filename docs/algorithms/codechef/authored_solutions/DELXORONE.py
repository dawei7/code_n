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
        freq = Counter(values)
        keep = 0
        for value in freq:
            keep = max(keep, freq[value] + freq.get(value ^ 1, 0))
        out.append(str(n - keep))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
