import sys

def window_beauty(values, left, size, pref, weighted):
    right = left + size
    total = pref[right] - pref[left]
    weighted_total = weighted[right] - weighted[left]
    return 2 * weighted_total - (2 * left + size - 1) * total

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, k = (data[idx], data[idx + 1])
        idx += 2
        values = data[idx:idx + n]
        idx += n
        values.sort()
        pref = [0] * (n + 1)
        weighted = [0] * (n + 1)
        for i, value in enumerate(values):
            pref[i + 1] = pref[i] + value
            weighted[i + 1] = weighted[i] + i * value
        best = min((window_beauty(values, left, k, pref, weighted) for left in range(n - k + 1)))
        out.append(str(best))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
