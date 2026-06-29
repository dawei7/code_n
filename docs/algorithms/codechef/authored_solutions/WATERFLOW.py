import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        w, x, y, z = data[idx], data[idx + 1], data[idx + 2], data[idx + 3]
        idx += 4
        total = w + y * z
        if total > x:
            out.append("overflow")
        elif total == x:
            out.append("filled")
        else:
            out.append("unfilled")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
