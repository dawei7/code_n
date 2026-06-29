import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, k = data[idx:idx + 2]
        idx += 2
        period = 3 * (k + 1) // 2
        full, rem = divmod(n, period)
        ans = 3 * full
        if rem >= 1:
            ans += 1
        if rem > k + 1:
            ans += 2
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
