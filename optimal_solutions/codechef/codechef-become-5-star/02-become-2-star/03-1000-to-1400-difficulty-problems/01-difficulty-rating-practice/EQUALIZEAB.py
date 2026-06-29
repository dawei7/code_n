import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        a, b, x = data[idx:idx + 3]
        idx += 3
        out.append('YES' if abs(a - b) % (2 * x) == 0 else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
