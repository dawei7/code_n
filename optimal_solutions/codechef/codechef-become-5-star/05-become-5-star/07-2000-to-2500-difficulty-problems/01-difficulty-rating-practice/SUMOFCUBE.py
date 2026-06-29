import sys
MOD = 998244353

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        pref = 0
        count = 1
        sum_p = 0
        sum_p2 = 0
        sum_p3 = 0
        ans = 0
        for value in data[idx:idx + n]:
            pref = (pref + value) % MOD
            ans = (ans + count * pref ** 3 - 3 * pref * pref * sum_p + 3 * pref * sum_p2 - sum_p3) % MOD
            count += 1
            sum_p = (sum_p + pref) % MOD
            sum_p2 = (sum_p2 + pref * pref) % MOD
            sum_p3 = (sum_p3 + pref * pref % MOD * pref) % MOD
        idx += n
        out.append(str(ans % MOD))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
