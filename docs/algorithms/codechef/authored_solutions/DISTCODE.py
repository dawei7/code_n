import sys


def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for s in data[1:1 + t]:
        out.append(str(len({s[i:i + 2] for i in range(len(s) - 1)})))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
