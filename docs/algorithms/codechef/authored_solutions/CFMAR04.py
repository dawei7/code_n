import sys
from collections import defaultdict


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    counts: dict[bytes, int] = defaultdict(int)
    best = 0
    for word in data[1:1 + n]:
        key = bytes(sorted(word))
        counts[key] += 1
        if counts[key] > best:
            best = counts[key]
    print(best)


if __name__ == "__main__":
    solve()
