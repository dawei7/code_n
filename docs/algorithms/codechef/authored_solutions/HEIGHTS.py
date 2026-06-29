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
        counts = [count for _, count in sorted(Counter(values).items())]
        single_positions = [i for i, count in enumerate(counts) if count == 1]
        singles = len(single_positions)
        if singles == 0:
            out.append("0")
        elif singles >= 2:
            out.append(str((singles + 1) // 2))
        else:
            pos = single_positions[0]
            has_higher_group = any(counts[i] >= 2 for i in range(pos + 1, len(counts)))
            has_lower_surplus = any(counts[i] >= 3 for i in range(pos))
            out.append("1" if has_higher_group or has_lower_surplus else "2")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
