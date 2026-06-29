import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        left = data[idx:idx + n]
        idx += n
        right = data[idx:idx + n]
        idx += n
        total = sum((min(right[i], left[i + 1]) for i in range(n - 1)))
        out.append(str(total))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
