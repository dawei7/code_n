from collections import Counter
import sys
MOD = 1000000007

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, k = data[idx:idx + 2]
        idx += 2
        arr = data[idx:idx + n]
        idx += n
        cnt = Counter((x % k for x in arr))
        ans = (cnt[0] + 1) % MOD
        for r in range(1, (k + 1) // 2):
            s = k - r
            ways = (pow(2, cnt[r], MOD) + pow(2, cnt[s], MOD) - 1) % MOD
            ans = ans * ways % MOD
        if k % 2 == 0:
            ans = ans * (cnt[k // 2] + 1) % MOD
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
