import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, m = data[idx:idx + 2]
        idx += 2
        arr = data[idx:idx + m]
        idx += m
        total = [0] * (n + 1)
        for x in arr:
            total[x] += 1
        inside = [0] * (n + 1)
        full = 0
        left = 0
        best_keep = 0
        for right, x in enumerate(arr):
            inside[x] += 1
            if inside[x] == total[x]:
                full += 1
            while full:
                y = arr[left]
                if inside[y] == total[y]:
                    full -= 1
                inside[y] -= 1
                left += 1
            best_keep = max(best_keep, right - left + 1)
        out.append(str(m - best_keep))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
