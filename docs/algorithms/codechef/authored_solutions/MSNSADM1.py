import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        goals = data[idx:idx + n]
        idx += n
        fouls = data[idx:idx + n]
        idx += n
        best = max(max(0, 20 * g - 10 * f) for g, f in zip(goals, fouls))
        out.append(str(best))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
