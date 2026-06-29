import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        arr = data[idx:idx + n]
        idx += n
        present = set(arr)
        missing = [x for x in range(1, 2 * n + 1) if x not in present]
        current_max = max(arr)
        prefix = [0]
        for value in missing:
            prefix.append(prefix[-1] + value)
        below_initial = 0
        while below_initial < len(missing) and missing[below_initial] < current_max:
            below_initial += 1
        best = -1
        if below_initial >= k:
            best = k * current_max - prefix[k]
        for pos, value in enumerate(missing):
            if value <= current_max:
                continue
            if pos >= k - 1:
                score = (k - 1) * value - prefix[k - 1]
                if score > best:
                    best = score
        out.append(str(best))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
