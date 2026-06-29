import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        a, b = data[idx], data[idx + 1]
        idx += 2
        out.append("YES" if a == b or b >= 2 * a else "NO")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
