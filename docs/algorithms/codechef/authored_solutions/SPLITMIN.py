from collections import defaultdict
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = []
        max_min = 0
        for pair_id in range(n):
            a, b = data[idx:idx + 2]
            idx += 2
            max_min = max(max_min, min(a, b))
            values.append((a, pair_id))
            values.append((b, pair_id))

        values.sort()
        freq = defaultdict(int)
        distinct = 0
        left = 0
        best = 10**30
        for right, (value, pair_id) in enumerate(values):
            if freq[pair_id] == 0:
                distinct += 1
            freq[pair_id] += 1
            while distinct >= 2:
                low = values[left][0]
                high = value
                if high >= max_min:
                    best = min(best, high - low)
                old_pair = values[left][1]
                freq[old_pair] -= 1
                if freq[old_pair] == 0:
                    distinct -= 1
                left += 1
        out.append(str(best))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
