import sys


def ceil_div2(value):
    return -((-value) // 2)


def score(a, b, x):
    return ceil_div2(b - x) + ceil_div2(x - a)


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        a, b = data[idx], data[idx + 1]
        idx += 2
        lo, hi = min(a, b), max(a, b)
        mid = (lo + hi) // 2
        candidates = {lo, hi}
        for x in range(mid - 3, mid + 4):
            if lo <= x <= hi:
                candidates.add(x)
        out.append(str(max(score(a, b, x) for x in candidates)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
