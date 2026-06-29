import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, boys, k = data[idx:idx + 3]
        idx += 3
        girls = n - boys
        out.append(str(abs((boys % k) - (girls % k))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
