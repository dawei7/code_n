import sys


def hours_needed(values, speed):
    return sum((value + speed - 1) // speed for value in values)


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, hours = data[idx], data[idx + 1]
        idx += 2
        values = data[idx:idx + n]
        idx += n
        lo, hi = 1, max(values)
        while lo < hi:
            mid = (lo + hi) // 2
            if hours_needed(values, mid) <= hours:
                hi = mid
            else:
                lo = mid + 1
        out.append(str(lo))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
