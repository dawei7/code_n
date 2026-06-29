import sys


def square_sum(pref, r: int, c: int, size: int) -> int:
    r2 = r + size
    c2 = c + size
    return pref[r2][c2] - pref[r][c2] - pref[r2][c] + pref[r][c]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, m, k = data[idx:idx + 3]
        idx += 3
        a = []
        for _ in range(n):
            a.append(data[idx:idx + m])
            idx += m

        pref = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            row_sum = 0
            prow = pref[i]
            crow = pref[i + 1]
            for j, value in enumerate(a[i], 1):
                row_sum += value
                crow[j] = prow[j] + row_sum

        ans = 0
        for size in range(1, n + 1):
            needed = k * size * size
            max_col = m - size
            for r in range(n - size + 1):
                lo, hi = 0, max_col + 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if square_sum(pref, r, mid, size) >= needed:
                        hi = mid
                    else:
                        lo = mid + 1
                if lo <= max_col:
                    ans += max_col - lo + 1
        out.append(str(ans))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
