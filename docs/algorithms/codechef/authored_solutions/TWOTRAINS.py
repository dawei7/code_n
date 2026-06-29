import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        times = data[idx:idx + n - 1]
        idx += n - 1
        out.append(str(sum(times) + max(times)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
