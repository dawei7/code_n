from collections import Counter
import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = sorted(data[idx:idx + n])
        idx += n
        if n < 3:
            out.append(' '.join(map(str, arr)))
            continue
        if max(Counter(arr).values()) > (n + 1) // 2:
            out.append('-1')
            continue

        def is_interesting(candidate):
            return all((not (candidate[i] <= candidate[i + 1] <= candidate[i + 2] or candidate[i] >= candidate[i + 1] >= candidate[i + 2]) for i in range(n - 2)))
        candidates = []
        low_count = (n + 1) // 2
        lows = arr[:low_count]
        highs = arr[low_count:]
        cand = [0] * n
        cand[0::2] = lows
        cand[1::2] = highs
        candidates.append(cand)
        high_count = (n + 1) // 2
        lows = arr[:n - high_count]
        highs = arr[n - high_count:]
        cand = [0] * n
        cand[0::2] = highs
        cand[1::2] = lows
        candidates.append(cand)
        for cand in candidates:
            if is_interesting(cand):
                out.append(' '.join(map(str, cand)))
                break
        else:
            out.append('-1')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
