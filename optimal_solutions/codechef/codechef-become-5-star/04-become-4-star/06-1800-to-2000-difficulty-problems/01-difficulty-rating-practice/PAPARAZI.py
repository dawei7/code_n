import sys

def should_pop(a, b, c, h) -> bool:
    return (h[b] - h[a]) * (c - b) <= (h[c] - h[b]) * (b - a)

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        h = data[idx:idx + n]
        idx += n
        hull = []
        ans = 1
        for i in range(n):
            while len(hull) >= 2 and should_pop(hull[-2], hull[-1], i, h):
                hull.pop()
            if hull:
                ans = max(ans, i - hull[-1])
            hull.append(i)
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
