import sys
MOD = 1000000007

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        dp = [0] * 7
        for _ in range(n):
            token = data[idx]
            idx += 1
            value = int(token) % 7
            power = pow(10, len(token), 7)
            new_dp = dp[:]
            new_dp[value] = (new_dp[value] + 1) % MOD
            for rem, ways in enumerate(dp):
                if ways:
                    nxt = (rem * power + value) % 7
                    new_dp[nxt] = (new_dp[nxt] + ways) % MOD
            dp = new_dp
        out.append(str(dp[0] % MOD))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
