import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, left, price = data[idx:idx + 3]
        idx += 3
        out.append(str(min(left, n - left) * price))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
