import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        x, y, step, _ = data[idx:idx + 4]
        idx += 4
        distance = abs(x - y)
        out.append('Yes' if distance % step == 0 and distance // step % 2 == 0 else 'No')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
