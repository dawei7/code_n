import sys


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    out = []
    idx = 1
    for _ in range(t):
        x = data[idx]
        y = data[idx + 1]
        idx += 2
        out.append(str(x ^ y))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
