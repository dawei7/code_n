import sys
from collections import defaultdict


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        by_length = defaultdict(list)
        for pos, value in enumerate(data[idx:idx + n], start=1):
            by_length[value].append(pos)
        idx += n

        answer = 0
        for length, positions in by_length.items():
            max_start = n - length + 1
            if max_start < 1:
                continue
            merged_right = 0
            for pos in positions:
                left = max(1, pos - length + 1)
                right = min(pos, max_start)
                if left > right:
                    continue
                if left > merged_right:
                    answer += right - left + 1
                    merged_right = right
                elif right > merged_right:
                    answer += right - merged_right
                    merged_right = right
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
