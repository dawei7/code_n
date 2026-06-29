import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, threshold = (data[idx], data[idx + 1])
        idx += 2
        values = data[idx:idx + n]
        idx += n
        out.append('YES' if max(values) >= threshold else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
