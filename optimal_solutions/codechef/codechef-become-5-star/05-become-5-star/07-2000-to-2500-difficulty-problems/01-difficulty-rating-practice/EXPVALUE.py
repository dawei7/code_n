import math
mod1 = 998244353

def mul(a, b):
    return a % mod1 * (b % mod1) % mod1

def binpow(a, b):
    if b == 0:
        return 1
    tmp = binpow(a, b // 2)
    tmp = mul(tmp, tmp)
    if b % 2:
        return mul(tmp, a)
    return tmp

def mod_inverse(a, m=mod1):
    return binpow(a, m - 2)

def solve():
    N, P = map(int, input().split())
    dp = [0] * (N + 1)
    dp2 = [0] * (N + 1)
    dp[1] = dp2[1] = mod_inverse(2)
    inv2 = mod_inverse(2)
    for i in range(1, N + 1):
        y = binpow(P, i - 1)
        y = mod_inverse(y)
        val = dp[i - 1] + mul(binpow(y, 2), inv2) + mul(y, dp2[i - 1])
        val %= mod1
        dp[i] = val
        dp2[i] = (dp2[i - 1] + mul(y, inv2)) % mod1
    print(*dp[1:])


if __name__ == "__main__":
    solve()
