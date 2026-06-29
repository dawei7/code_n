import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, k = data[idx:idx + 2]
        idx += 2
        half = n // 2
        minimum = half * 1 + half * 2
        maximum = half * 99999 + half * 100000
        if k < minimum or k > maximum or (k - minimum) % 2:
            out.append('-1')
            continue
        arr = [1] * half + [2] * half
        extra = k - minimum
        for i in range(n):
            add = min(extra, 99998)
            arr[i] += add
            extra -= add
            if extra == 0:
                break
        out.append(' '.join(map(str, arr)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
