import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        a, b, c, d = data[idx:idx + 4]
        idx += 4
        total = b - a + 1 + (d - c + 1)
        overlap = max(0, min(b, d) - max(a, c) + 1)
        out.append(str(total - overlap))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
