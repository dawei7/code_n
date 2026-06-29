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
        frequency_counts = Counter(Counter(values).values())
        best_count = max(frequency_counts.values())
        out.append(str(min((freq for freq, count in frequency_counts.items() if count == best_count))))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
