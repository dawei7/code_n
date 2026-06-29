import sys


def enough(values, x, y, blimps):
    suffix_hits = 0
    for sadness in reversed(values):
        remaining = sadness - suffix_hits * y
        if remaining <= 0:
            continue
        if x <= y:
            return False
        need = (remaining + x - 1) // x
        suffix_hits += need
        if suffix_hits > blimps:
            return False
    return True


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, x, y = data[idx:idx + 3]
        idx += 3
        values = data[idx:idx + n]
        idx += n
        if x <= y:
            out.append(str(max((value + y - 1) // y for value in values)))
            continue
        lo, hi = 0, max((value + min(x, y) - 1) // min(x, y) for value in values) + n
        while lo < hi:
            mid = (lo + hi) // 2
            if enough(values, x, y, mid):
                hi = mid
            else:
                lo = mid + 1
        out.append(str(lo))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
