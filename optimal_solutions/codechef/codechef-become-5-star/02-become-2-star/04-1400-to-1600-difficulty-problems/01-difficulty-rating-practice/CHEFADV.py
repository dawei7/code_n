import sys

def reachable(n, m, x, y):
    return (n - 1) % x == 0 and (m - 1) % y == 0 or (n >= 2 and m >= 2 and ((n - 2) % x == 0) and ((m - 2) % y == 0))

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, m, x, y = data[idx:idx + 4]
        idx += 4
        out.append('Chefirnemo' if reachable(n, m, x, y) else 'Pofik')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
