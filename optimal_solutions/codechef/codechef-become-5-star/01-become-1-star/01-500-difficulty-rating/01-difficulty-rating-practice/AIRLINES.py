import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        x, y, z = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        out.append(str(min(10 * x, y) * z))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
