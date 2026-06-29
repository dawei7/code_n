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
        if 0 in values or sum(1 for value in values if value < 0) % 2 == 0:
            out.append("0")
        else:
            out.append("1")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
