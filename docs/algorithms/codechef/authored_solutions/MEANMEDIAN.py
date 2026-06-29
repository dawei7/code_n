import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        mean, median = data[idx], data[idx + 1]
        idx += 2
        out.append(f"{median} {median} {3 * mean - 2 * median}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
