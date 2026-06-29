import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        lis = data[idx:idx + n]
        idx += n
        out.append(''.join(map(str, lis)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
