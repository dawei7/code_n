import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    base = 50001
    for n in data[1:1 + t]:
        out.append(" ".join(str(base + i) for i in range(n)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
