import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        c = int(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        positions = [i for i, ch in enumerate(s) if ch == 49]
        if len(positions) <= 1:
            out.append('YES')
            continue
        gaps = []
        for a, b in zip(positions, positions[1:]):
            gaps.append(b - a - 1)
        gaps.append(positions[0] + n - positions[-1] - 1)
        out.append('YES' if sum((gap > c for gap in gaps)) <= 1 else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
