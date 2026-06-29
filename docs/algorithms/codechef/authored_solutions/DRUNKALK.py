import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for k in data[1:1 + t]:
        out.append(str((k // 2) * 2 + (3 if k % 2 else 0)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
