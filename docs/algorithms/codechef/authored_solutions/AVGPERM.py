import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for n in data[1:1 + t]:
        weights = [1] * n
        if n >= 2:
            weights[1] += 1
            weights[-2] += 1
        for i in range(2, n - 2):
            weights[i] += 2
        positions = sorted(range(n), key=lambda i: (-weights[i], i))
        perm = [0] * n
        for value, pos in enumerate(positions, start=1):
            perm[pos] = value
        out.append(" ".join(map(str, perm)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
