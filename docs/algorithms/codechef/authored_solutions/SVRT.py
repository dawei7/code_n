import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, k = data[idx], data[idx + 1]
        idx += 2
        distance = (n + k - 1) // k
        pairs = n - k * (distance - 1)
        out.append(f"{distance} {pairs}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
