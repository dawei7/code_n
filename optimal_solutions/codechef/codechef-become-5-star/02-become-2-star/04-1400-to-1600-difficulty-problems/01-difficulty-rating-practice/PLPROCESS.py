import sys

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
        total = sum(values)
        prefix = 0
        best = total
        for value in values:
            best = min(best, max(prefix, total - prefix))
            prefix += value
        best = min(best, max(prefix, total - prefix))
        out.append(str(best))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
