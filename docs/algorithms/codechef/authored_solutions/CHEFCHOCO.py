import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        c, x, y = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        out.append(str((c - x) * y))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
