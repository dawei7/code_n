import sys


MOD = 1000000007


def count_ways(n, limit):
    if n % 2:
        return 0
    target = n // 2
    max_part = limit // 2
    if max_part <= 0:
        return 0
    dp = [0] * (target + 1)
    dp[0] = 1
    window = 0
    for total in range(1, target + 1):
        window = (window + dp[total - 1]) % MOD
        if total - max_part - 1 >= 0:
            window = (window - dp[total - max_part - 1]) % MOD
        dp[total] = window
    return dp[target]


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, limit = data[idx], data[idx + 1]
        idx += 2
        out.append(str(count_ways(n, limit)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
