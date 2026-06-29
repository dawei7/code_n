import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, mod = data[idx], data[idx + 1]
        idx += 2
        values = data[idx:idx + n]
        idx += n
        count = sum(1 for value in values if value % mod == 0)
        out.append(str((1 << count) - 1))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
