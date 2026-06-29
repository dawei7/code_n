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
        arr = data[idx:idx + n]
        idx += n
        max_freq = max(Counter(arr).values(), default=1)
        out.append(str((max_freq - 1).bit_length()))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
