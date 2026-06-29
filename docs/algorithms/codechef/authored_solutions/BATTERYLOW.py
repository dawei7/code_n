import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = ["Yes" if data[i] <= 15 else "No" for i in range(1, t + 1)]
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
