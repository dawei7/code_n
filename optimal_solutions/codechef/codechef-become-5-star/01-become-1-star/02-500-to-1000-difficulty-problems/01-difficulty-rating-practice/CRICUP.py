import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        x, y, d = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        out.append('YES' if abs(x - y) <= d else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
