import sys
MOD = 1000000007

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        dishes, cooks = (data[idx], data[idx + 1])
        idx += 2
        dp = [0] * (dishes + 1)
        dp[0] = 1
        for _cook in range(cooks):
            low, high = (data[idx], data[idx + 1])
            idx += 2
            ndp = [0] * (dishes + 1)
            window = 0
            for total in range(dishes + 1):
                if total - low >= 0:
                    window = (window + dp[total - low]) % MOD
                if total - high - 1 >= 0:
                    window = (window - dp[total - high - 1]) % MOD
                ndp[total] = window
            dp = ndp
        out.append(str(dp[dishes] % MOD))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
