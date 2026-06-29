import sys


def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for token in data[1:1 + t]:
        out.append(str(int(token[::-1])))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
