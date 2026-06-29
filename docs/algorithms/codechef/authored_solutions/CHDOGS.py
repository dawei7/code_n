import sys


def solve():
    data = list(map(float, sys.stdin.buffer.read().split()))
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        side, speed = data[idx], data[idx + 1]
        idx += 2
        out.append(f"{2 * side / (3 * speed):.10f}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
