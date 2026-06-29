import sys
from collections import Counter


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        freq = Counter(data[idx:idx + n])
        idx += n
        odd = sum(count & 1 for count in freq.values())
        total_after_pairs = n + odd
        extra = odd
        if total_after_pairs % 4:
            extra += 2
        out.append(str(extra))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
