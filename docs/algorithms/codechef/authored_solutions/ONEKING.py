import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        intervals = []
        for _ in range(n):
            left, right = data[idx], data[idx + 1]
            idx += 2
            intervals.append((right, left))
        intervals.sort()
        bombs = 0
        last = -1
        for right, left in intervals:
            if left > last:
                bombs += 1
                last = right
        out.append(str(bombs))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
