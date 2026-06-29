import sys
MOD = 998244353

def build_factorials(limit: int):
    fact = [1] * (limit + 1)
    for i in range(1, limit + 1):
        fact[i] = fact[i - 1] * i % MOD
    invfact = [1] * (limit + 1)
    invfact[limit] = pow(fact[limit], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD
    return (fact, invfact)

def comb(n: int, r: int, fact, invfact) -> int:
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pairs = [(data[i], data[i + 1]) for i in range(1, 2 * t + 1, 2)]
    limit = max((n + m for n, m in pairs)) + 5
    fact, invfact = build_factorials(limit)
    out = []
    for n, m in pairs:
        path_len = n + m - 1
        if path_len % 2:
            out.append('0')
            continue
        paths = comb(n + m - 2, n - 1, fact, invfact)
        balanced = comb(path_len, path_len // 2, fact, invfact)
        free = n * m - path_len
        ans = paths * balanced % MOD * pow(2, free, MOD) % MOD
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
