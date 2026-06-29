import sys
from array import array
MOD = 1000000007

def expected_value(n: int, m: int) -> int:
    if m == 0:
        return 0
    if n == 1:
        return 1
    limit = n - 1
    block = max(1, int(limit ** 0.5))
    inv = [0] * (limit + 1)
    for i in range(1, limit + 1):
        inv[i] = pow(i, MOD - 2, MOD)
    dp = [0] * (limit + 1)
    prefixes = [array('I', [0]) for _ in range(block + 1)]
    for x in range(1, limit + 1):
        total = 0
        r = 1
        while r <= x:
            q = x // r
            right = x // q
            if q <= block:
                high = x - q * r
                low = x - q * right
                pref = prefixes[q]
                subtotal = pref[high]
                if low >= q:
                    subtotal -= pref[low - q]
                total += subtotal
            else:
                for div in range(r, right + 1):
                    total += dp[x % div]
            total %= MOD
            r = right + 1
        dp[x] = (n + total) * inv[x] % MOD
        value = dp[x]
        for q in range(1, block + 1):
            pref = prefixes[q]
            previous = pref[x - q] if x >= q else 0
            pref.append((previous + value) % MOD)
    if m <= limit:
        return dp[m]
    total = 0
    for r in range(1, n + 1):
        total += dp[m % r]
        if total >= 1 << 63:
            total %= MOD
    return (1 + total % MOD * pow(n, MOD - 2, MOD)) % MOD

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    print(expected_value(data[0], data[1]))


if __name__ == "__main__":
    solve()
