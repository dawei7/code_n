import sys
from collections import Counter


def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for s in data[1:1 + t]:
        counts = Counter(s)
        odd = sum(1 for count in counts.values() if count % 2)
        pairs = sum(count // 2 for count in counts.values())
        out.append("YES" if pairs >= odd else "NO")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
