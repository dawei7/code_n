import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        x, y, xr, yr, days = data[idx:idx + 5]
        idx += 5
        out.append("YES" if x >= xr * days and y >= yr * days else "NO")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
