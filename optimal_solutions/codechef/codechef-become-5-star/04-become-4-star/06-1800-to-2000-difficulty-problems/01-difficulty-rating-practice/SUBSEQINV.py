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
        p = data[idx:idx + n]
        idx += n
        prefix_max = [0] * n
        mx = 0
        for i, value in enumerate(p):
            prefix_max[i] = mx
            mx = max(mx, value)
        suffix_min = [n + 1] * n
        mn = n + 1
        for i in range(n - 1, -1, -1):
            suffix_min[i] = mn
            mn = min(mn, p[i])
        mandatory = 0
        for i, value in enumerate(p):
            if prefix_max[i] > value or suffix_min[i] < value:
                mandatory += 1
        free = n - mandatory
        ans = pow(2, free, MOD)
        if mandatory == 0:
            ans = (ans - 1) % MOD
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
