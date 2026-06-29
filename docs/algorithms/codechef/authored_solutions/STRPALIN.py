import sys


def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        a = set(data[idx])
        b = set(data[idx + 1])
        idx += 2
        out.append("Yes" if a & b else "No")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
